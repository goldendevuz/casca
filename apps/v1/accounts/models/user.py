from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.v1.shared.enums import AuthStatuses


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        if not password:
            raise ValueError("The password must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        blank=True,
        null=True,
    )
    email = models.EmailField(_("email address"), blank=True, null=True)
    phone = models.CharField(_("phone"), max_length=13, blank=True, null=True)
    auth_status = models.CharField(
        _("Auth Status"),
        max_length=20,
        choices=AuthStatuses.choices,
        default=AuthStatuses.NEW,
    )
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    password = models.CharField(_("password"), max_length=128)

    objects = UserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("accounts")
        ordering = ["-date_joined"]

    def __str__(self):
        return self.username or str(self.id)
