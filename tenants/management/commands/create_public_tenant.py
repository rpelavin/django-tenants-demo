from django.core.management.base import BaseCommand
from tenants.models import Tenant, Domain

class Command(BaseCommand):
    help = 'Creates the public tenant if it does not already exist'

    def add_arguments(self, parser):
        parser.add_argument('--public-tenant-domain', required=True, help='The public tenant domain.')
        parser.add_argument('--superuser-username', required=True, help='The superuser username.')
        parser.add_argument('--superuser-email', required=True, help='The superuser email.')
        parser.add_argument('--superuser-password', required=True, help='The superuser password.')

    def handle(self, *args, **options):
        if not Tenant.objects.filter(schema_name='public').exists():
            tenant = Tenant(schema_name='public',
                            superuser_username=options['superuser_username'],
                            superuser_email=options['superuser_email'],
                            superuser_password=options['superuser_password'])
            tenant.save()
            domain = Domain(domain=options['public_tenant_domain'],
                            tenant=tenant,
                            is_primary=True)
            domain.save()
            self.stdout.write(self.style.SUCCESS('Created public tenant.'))
        else:
            self.stdout.write(self.style.SUCCESS('Found public tenant.'))