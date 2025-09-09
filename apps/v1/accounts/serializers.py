import random
import string

from django.db.models import Q
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.validators import FileExtensionValidator, validate_email
from icecream import ic

from apps.v1.shared.enums import AuthStatuses, AuthTypes
from apps.v1.shared.utils.verification import VerificationService
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.exceptions import ValidationError, PermissionDenied, NotFound
from django.utils.translation import gettext_lazy as _

from apps.v1.shared.utility import check_username_phone_email, send_email, send_phone_code, check_user_type, phone_regex
from .models import Profile, User, UserConfirmation

# --------------------
# Profile Nested Serializers
# --------------------
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"



# --------------------
# User Response Serializer (output)
# --------------------
class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
            "created",
            "modified",
            "email",
            "phone",
            "auth_status",
            "username",
        ]


# --------------------
# SignUp Serializer (main)
# --------------------
class SignUpSerializer(serializers.Serializer):
    username_phone_email = serializers.CharField(required=True, write_only=True)

    # internal fields (set in validate, not provided by client)
    verify_type = serializers.CharField(read_only=True)
    verify_value = serializers.CharField(read_only=True)

    def create(self, validated_data):
        verify_type = validated_data.get("verify_type")
        verify_value = validated_data.get("verify_value")

        if not verify_type or not verify_value:
            raise ValidationError({"message": "verify_type or verify_value missing"})

        from apps.v1.accounts.views import PasswordGeneratorView
        password_response = PasswordGeneratorView.generate_password()
        password = password_response["password"]

        username = self.generate_username()

        user = User(username=username)
        user.set_password(password)

        user.save()

        VerificationService.create_and_send_code(
            user=user,
            verify_type=verify_type,
            verify_value=verify_value
        )

        return user

    @staticmethod
    def generate_username(length: int = 8):
        letters_digits = string.ascii_lowercase + string.digits
        return "user_" + "".join(random.choices(letters_digits, k=length))

    def validate(self, data):
        data = super().validate(data)
        return self.auth_validate(data)

    @staticmethod
    def auth_validate(data):
        user_input = str(data.get("username_phone_email")).lower()
        input_type = check_username_phone_email(user_input)

        if input_type == "email":
            try:
                validate_email(user_input)
            except ValidationError:
                raise ValidationError({"message": "Invalid email address"})
            data["verify_type"] = AuthTypes.VIA_EMAIL
            data["verify_value"] = user_input

        elif input_type == "phone":
            if not phone_regex.match(user_input):
                raise ValidationError({"message": "Invalid phone number format"})
            data["verify_type"] = AuthTypes.VIA_PHONE
            data["verify_value"] = user_input

        else:
            raise ValidationError({"message": "You must send a valid email or phone number"})

        return data

    def to_representation(self, instance):
        return {
                "user": UserResponseSerializer(instance).data,
                "next_step": str(_("Verify code sent to your email or phone")),
                **(instance.token() if callable(getattr(instance, "token", None)) else {})
            }


# --------------------
# (other serializers left unchanged; included here for completeness)
# --------------------
class UpdateUserInformation(serializers.Serializer):
    # User fields
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    # Profile fields
    full_name = serializers.CharField(write_only=True, required=True)
    gender = serializers.ChoiceField(
        write_only=True,
        required=True,
        choices=[("male", "Male"), ("female", "Female")],
    )
    birth_date = serializers.DateField(write_only=True, required=True)
    avatar = serializers.ImageField(write_only=True, required=False, allow_null=True)

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError(
                {"message": "Parolingiz va tasdiqlash parolingiz bir-biriga teng emas"}
            )
        if password:
            validate_password(password)

        return data

    def validate_username(self, username):
        if len(username) < 5 or len(username) > 30:
            raise ValidationError(
                {"message": "Username must be between 5 and 30 characters long"}
            )
        if username.isdigit():
            raise ValidationError(
                {"message": "This username is entirely numeric"}
            )
        return username

    def update(self, instance, validated_data):
        """
        instance → User object
        instance.profile → related Profile object
        """

        # Update User
        instance.username = validated_data.get("username", instance.username)
        if validated_data.get("password"):
            instance.set_password(validated_data["password"])

        # Update Profile
        profile = instance.profile
        profile.full_name = validated_data.get("full_name", profile.full_name)
        profile.gender = validated_data.get("gender", profile.gender)
        profile.birth_date = validated_data.get("birth_date", profile.birth_date)

        avatar = validated_data.get("avatar")
        if avatar is not None:  # update only if provided
            profile.avatar = avatar

        profile.save()

        # Update auth_status if needed
        if instance.auth_status == AuthStatuses.CODE_VERIFIED:
            instance.auth_status = AuthStatuses.DONE

        instance.save()
        return instance


class UpdateUserPhotoSerializer(serializers.Serializer):
    photo = serializers.ImageField(validators=[FileExtensionValidator(allowed_extensions=[
        'jpg', 'jpeg', 'png', 'heic', 'heif'
    ])])

    def update(self, instance, validated_data):
        photo = validated_data.get('photo')
        if photo:
            instance.photo = photo
            instance.auth_status = AuthStatuses.DONE
            instance.save()

        return instance


class LoginSerializer(TokenObtainPairSerializer):

    def __init__(self, *args, **kwargs):
        super(LoginSerializer, self).__init__(*args, **kwargs)
        self.fields['userinput'] = serializers.CharField(required=True)
        self.fields['username'] = serializers.CharField(required=False, read_only=True)

    def auth_validate(self, data):
        user_input = data.get('userinput')  # email, phone, username
        if check_user_type(user_input) == 'username':
            username = user_input
        elif check_user_type(user_input) == "email":  # Anora@gmail.com   -> anOra@gmail.com
            user = self.get_user(email__iexact=user_input) # user get method orqali user o'zgartiruvchiga biriktirildi
            username = user.username
        elif check_user_type(user_input) == 'phone':
            user = self.get_user(phone=user_input)
            username = user.username
        else:
            data = {
                'success': True,
                'message': "Siz email, username yoki telefon raqami jonatishingiz kerak"
            }
            raise ValidationError(data)

        authentication_kwargs = {
            self.username_field: username,
            'password': data['password']
        }
        # user statusi tekshirilishi kerak
        current_user = User.objects.filter(username__iexact=username).first()  # None

        if current_user is not None and current_user.auth_status in [AuthStatuses.NEW, AuthStatuses.CODE_VERIFIED]:
            raise ValidationError(
                {
                    'message': "Siz royhatdan toliq otmagansiz!"
                }
            )
        user = authenticate(**authentication_kwargs)
        if user is not None:
            self.user = user
        else:
            raise ValidationError({
                'message': _("The login or password you entered is incorrect. Please check and try again.")
            })

    def validate(self, data):
        self.auth_validate(data)
        if self.user.auth_status not in [AuthStatuses.DONE, AuthStatuses.DONE]:
            raise PermissionDenied("Siz login qila olmaysiz. Ruxsatingiz yoq")
        data = self.user.token()
        data['auth_status'] = self.user.auth_status
        return data


class LoginRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        try:
            refresh = RefreshToken(attrs['refresh'])
        except TokenError:
            raise ValidationError({'refresh': "Token noto'g'ri yoki muddati tugagan"})

        data = {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }
        return data


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class ResetPasswordSerializer(serializers.Serializer):
    username_phone_email = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        username_phone_email = attrs.get('username_phone_email', None)
        if username_phone_email is None:
            raise ValidationError(
                {
                    'message': "Email yoki telefon raqami kiritilishi shart!"
                }
            )
        user = User.objects.filter(Q(phone=username_phone_email) | Q(email=username_phone_email))
        if not user.exists():
            raise NotFound(detail="User not found")
        attrs['user'] = user.first()
        return attrs


class ForgetPasswordSerializer(serializers.Serializer):
    verify_type = serializers.ChoiceField(choices=['AuthTypes.via_email', 'AuthTypes.via_phone'])
    verify_value = serializers.CharField()

    def validate(self, attrs):
        verify_type = attrs.get('verify_type')
        verify_value = attrs.get('verify_value')

        # verify_type ga qarab, qayerdan izlash kerakligini aniqlaymiz
        if verify_type == 'AuthTypes.VIA_EMAIL':
            user = User.objects.filter(email__iexact=verify_value).first()
        else:
            user = User.objects.filter(phone=verify_value).first()

        if not user:
            raise serializers.ValidationError("Bunday foydalanuvchi topilmadi.")
        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        user = validated_data['user']
        verify_type = validated_data['verify_type']
        verify_value = validated_data['verify_value']

        # Eski, tasdiqlanmagan kodlarni o'chirish (ixtiyoriy)
        UserConfirmation.objects.filter(
            user=user,
            verify_type=verify_type,
            is_confirmed=False
        ).delete()

        code = user.create_verify_code(
            verify_type=verify_type,
            verify_value=verify_value
        )
        # Bu yerda kodni yuborish uchun email yoki sms jo'natish funksiyasini chaqirishingiz mumkin

        return {'message': 'Tasdiqlash kodi yuborildi.', 'code': code if True else 'hidden'}
