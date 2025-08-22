from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from domain.entities.models.barbershop import Barbershop, Specialty, Service, Banner, ContactUs
from .shared import BaseAdmin


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
