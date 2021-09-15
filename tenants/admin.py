from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Tenant, Domain

class DomainInline(admin.TabularInline):
    model = Domain

@admin.register(Tenant)
class TenantAdmin(TenantAdminMixin, admin.ModelAdmin):
    inlines = [DomainInline]
    list_display = ('schema_name',)