from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Tenant(TenantMixin):
    auto_create_schema = True

    def __str__(self):
        return self.schema_name


class Domain(DomainMixin):
    def __str__(self):
        return self.domain