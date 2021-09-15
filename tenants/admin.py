from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from common.mixins import PublicAdminOnlyMixin
from .models import Tenant, Domain

class DomainInline(admin.TabularInline):
    model = Domain

@admin.register(Tenant)
class TenantAdmin(PublicAdminOnlyMixin, TenantAdminMixin, admin.ModelAdmin):
    inlines = [DomainInline]
    list_display = ('schema_name',)