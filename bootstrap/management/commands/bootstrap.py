from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from tenants.models import Tenant, Domain

class Command(BaseCommand):
    help = 'Bootstraps the environment with default development data'

    def handle(self, *args, **options):
        # Ensure superuser created
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(username='admin',
                                          email='admin@local',
                                          password='password')
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

        # Ensure public domain created
        if not Domain.objects.filter(domain='localhost').exists():
            domain = Domain()
            domain.domain = 'localhost'
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()
            self.stdout.write(self.style.SUCCESS('Created localhost domain.'))
        else:
            self.stdout.write(self.style.SUCCESS('Found localhost domain.'))