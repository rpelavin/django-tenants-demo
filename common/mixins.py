from django_tenants.utils import get_public_schema_name


class PublicAdminOnlyMixin():
    def has_add_permission(self, request, obj=None):
        return request.tenant.schema_name == get_public_schema_name()

    def has_delete_permission(self, request, obj=None):
        return request.tenant.schema_name == get_public_schema_name()

    def has_view_or_change_permission(self, request, obj=None):
        return request.tenant.schema_name == get_public_schema_name()

    def has_module_permission(self, request):
        return request.tenant.schema_name == get_public_schema_name()


class NotPublicAdminOnlyMixin():
    def has_add_permission(self, request, obj=None):
        return not request.tenant.schema_name == get_public_schema_name()

    def has_delete_permission(self, request, obj=None):
        return not request.tenant.schema_name == get_public_schema_name()

    def has_view_or_change_permission(self, request, obj=None):
        return not request.tenant.schema_name == get_public_schema_name()

    def has_module_permission(self, request):
        return not request.tenant.schema_name == get_public_schema_name()