from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from tenants.models import Tenant, Domain

class Command(BaseCommand):
    help = 'Bootstraps the environment with default development data'

    def add_arguments(self, parser):
        parser.add_argument('--admin-username', required=True, help='The admin username.')
        parser.add_argument('--admin-email', required=True, help='The admin email.')
        parser.add_argument('--admin-password', required=True, help='The admin password.')
        parser.add_argument('--public-tenant-domain', required=True, help='The public tenant domain.')

    def handle(self, *args, **options):
        # Ensure admin superuser created
        User = get_user_model()
        if not User.objects.filter(username=options['admin_username']).exists():
            User.objects.create_superuser(username=options['admin_username'],
                                          email=options['admin_email'],
                                          password=options['admin_password'])
            self.stdout.write(self.style.SUCCESS('Created admin superuser.'))
        else:
            self.stdout.write(self.style.SUCCESS('Found admin superuser.'))
        
        # Ensure public tenant created
        if not Tenant.objects.filter(name='public').exists():
            tenant = Tenant(schema_name='public',
                            name='public')
            tenant.save()
            self.stdout.write(self.style.SUCCESS('Created public tenant.'))
        else:
            self.stdout.write(self.style.SUCCESS('Found public tenant.'))

        # Ensure public tenant domain created
        if not Domain.objects.filter(domain='localhost').exists():
            domain = Domain(domain=options['public_tenant_domain'],
                            tenant=tenant,
                            is_primary = True)
            domain.save()
            self.stdout.write(self.style.SUCCESS('Created localhost domain.'))
        else:
            self.stdout.write(self.style.SUCCESS('Found localhost domain.'))