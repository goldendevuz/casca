from django import forms
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from core.domain.entities.models.appointment import *
from core.domain.entities.models.barber import *
from core.domain.entities.models.barbershop import *
from core.domain.entities.models.system import *
from core.domain.entities.models.user import *

class BaseAdmin(admin.ModelAdmin):
    list_per_page = 10
    class Meta:
        abstract = True

class UserConfirmationResource(resources.ModelResource):
    class Meta:
        model = UserConfirmation

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ()

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [ProfileResource]
    list_display = tuple(f.name for f in Profile._meta.fields if f.name not in ('id',))
    list_filter = ('gender',)
    search_fields = ('user__username',)

@admin.register(UserConfirmation)
class UserConfirmationAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [UserConfirmationResource]
    list_display = tuple(f.name for f in UserConfirmation._meta.fields if f.name not in ('id',))
    list_filter = ('verify_type', 'is_confirmed')
    search_fields = ('verify_value', 'user__username')

@admin.register(User)
class UserAdmin(ImportExportModelAdmin, BaseAdmin):
    form = CustomUserForm
    resource_classes = [UserResource]
    list_display = tuple(f.name for f in User._meta.fields if f.name not in ('password', 'is_staff', 'is_superuser', 'id'))
    search_fields = ('username', 'email', 'phone')
    list_filter = ('role', 'auth_status', 'is_active')

####################################################################################################################
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class NotificationResource(resources.ModelResource):
    class Meta:
        model = Notification

class NotificationSettingResource(resources.ModelResource):
    class Meta:
        model = NotificationSetting

class PaymentResource(resources.ModelResource):
    class Meta:
        model = Payment

@admin.register(Notification)
class NotificationAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [NotificationResource]
    list_display = tuple(f.name for f in Notification._meta.fields if f.name not in ('id',))
    list_filter = ()
    search_fields = ('title', 'message')

@admin.register(NotificationSetting)
class NotificationSettingAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [NotificationSettingResource]
    list_display = tuple(f.name for f in NotificationSetting._meta.fields if f.name not in ('id',))
    list_filter = ()
    search_fields = ('user__username',)

@admin.register(Payment)
class PaymentAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [PaymentResource]
    list_display = tuple(f.name for f in Payment._meta.fields if f.name not in ('id',))
    list_filter = ('status', 'method')
    search_fields = ('transaction_id', 'user__username')

####################################################################################################################
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class BannerResource(resources.ModelResource):
    class Meta:
        model = Banner

class ContactUsResource(resources.ModelResource):
    class Meta:
        model = ContactUs

class BarbershopResource(resources.ModelResource):
    class Meta:
        model = Barbershop

class ServiceResource(resources.ModelResource):
    class Meta:
        model = Service

class SpecialtyResource(resources.ModelResource):
    class Meta:
        model = Specialty

@admin.register(Banner)
class BannerAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [BannerResource]
    list_display = tuple(f.name for f in Banner._meta.fields if f.name not in ('id',))
    list_filter = ('is_active',)
    search_fields = ('title',)
    ordering = ('title',)

@admin.register(ContactUs)
class ContactUsAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [ContactUsResource]
    list_display = tuple(f.name for f in ContactUs._meta.fields if f.name not in ('id',))
    list_filter = ()
    search_fields = ('email', 'subject')

@admin.register(Barbershop)
class BarbershopAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [BarbershopResource]
    list_display = tuple(f.name for f in Barbershop._meta.fields if f.name not in ('id',))
    list_filter = ()
    search_fields = ('name', 'address')
    ordering = ('name',)

@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [ServiceResource]
    list_display = tuple(f.name for f in Service._meta.fields if f.name not in ('id',))
    list_filter = ('is_active',)
    search_fields = ('name',)
    ordering = ('title',)

@admin.register(Specialty)
class SpecialtyAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [SpecialtyResource]
    list_display = tuple(f.name for f in Specialty._meta.fields if f.name not in ('id',))
    list_filter = ()
    search_fields = ('name',)
    ordering = ('name',)

####################################################################################################################
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class BarberResource(resources.ModelResource):
    class Meta:
        model = Barber

class FavoriteResource(resources.ModelResource):
    class Meta:
        model = Favorite

class HistoryResource(resources.ModelResource):
    class Meta:
        model = History

class SecuritySettingResource(resources.ModelResource):
    class Meta:
        model = SecuritySetting

class WorkingHourResource(resources.ModelResource):
    class Meta:
        model = WorkingHour

@admin.register(Barber)
class BarberAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [BarberResource]
    list_display = tuple(f.name for f in Barber._meta.fields if f.name not in ('id',))
    list_filter = ('specialty',)
    search_fields = ('owner__username', 'owner__email', 'specialty__name')

@admin.register(Favorite)
class FavoriteAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [FavoriteResource]
    list_display = tuple(f.name for f in Favorite._meta.fields if f.name not in ('id',))
    list_filter = ('barber', 'user')
    search_fields = ('user__username', 'barber__owner__username')

@admin.register(History)
class HistoryAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [HistoryResource]
    list_display = tuple(f.name for f in History._meta.fields if f.name not in ('id',))
    list_filter = ('barber', 'action')
    search_fields = ('barber__owner__username', 'action')

@admin.register(SecuritySetting)
class SecuritySettingAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [SecuritySettingResource]
    list_display = tuple(f.name for f in SecuritySetting._meta.fields if f.name not in ('id',))
    list_filter = ('user',)
    search_fields = ('user__username',)

@admin.register(WorkingHour)
class WorkingHourAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [WorkingHourResource]
    list_display = tuple(f.name for f in WorkingHour._meta.fields if f.name not in ('id',))
    list_filter = ('barber', 'day_of_week')
    search_fields = ('barber__owner__username',)
    ordering = ('barber', 'day_of_week')

####################################################################################################################

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class AppointmentResource(resources.ModelResource):
    class Meta:
        model = Appointment

class RateResource(resources.ModelResource):
    class Meta:
        model = Rate

class ReasonResource(resources.ModelResource):
    class Meta:
        model = Reason

class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review

class ReviewLikeResource(resources.ModelResource):
    class Meta:
        model = ReviewLike

@admin.register(Appointment)
class AppointmentAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [AppointmentResource]
    list_display = tuple(f.name for f in Appointment._meta.fields if f.name not in ('id',))
    list_filter = ('status', 'barber', 'date')
    search_fields = ('barber__owner__username', 'patient__username', 'status')
    ordering = ('-date',)

@admin.register(Rate)
class RateAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [RateResource]
    list_display = tuple(f.name for f in Rate._meta.fields if f.name not in ('id',))
    list_filter = ()
    search_fields = ('appointment__barber__owner__username', 'appointment__patient__username')

@admin.register(Reason)
class ReasonAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [ReasonResource]
    list_display = tuple(f.name for f in Reason._meta.fields if f.name not in ('id',))
    list_filter = ()
    search_fields = ('description',)

@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [ReviewResource]
    list_display = tuple(f.name for f in Review._meta.fields if f.name not in ('id',))
    list_filter = ('appointment', 'rating')
    search_fields = ('appointment__barber__owner__username', 'appointment__patient__username', 'comment')

@admin.register(ReviewLike)
class ReviewLikeAdmin(ImportExportModelAdmin, BaseAdmin):
    resource_classes = [ReviewLikeResource]
    list_display = tuple(f.name for f in ReviewLike._meta.fields if f.name not in ('id',))
    list_filter = ('review', 'user')
    search_fields = ('review__comment', 'user__username')