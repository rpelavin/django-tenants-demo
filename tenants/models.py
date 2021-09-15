from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django_tenants.models import TenantMixin, DomainMixin
from django_tenants.signals import post_schema_sync
from django_tenants.utils import schema_context


class Tenant(TenantMixin):
    superuser_username = models.CharField(max_length=100)
    superuser_email = models.EmailField()
    superuser_password = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True

    def __str__(self):
        return self.schema_name


class Domain(DomainMixin):
    def __str__(self):
        return self.domain


@receiver(post_schema_sync, sender=TenantMixin)
def create_tenant_superuser(tenant, **kwargs):
    with schema_context(tenant.schema_name):
        User.objects.create_user(username=tenant.superuser_username,
                                 email=tenant.superuser_email,
                                 password=tenant.superuser_password,
                                 is_staff=True,
                                 is_superuser=True)