from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .shared import BaseAdmin
from domain.entities.models.barber import Barber, Favorite, History, SecuritySetting, WorkingHour

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