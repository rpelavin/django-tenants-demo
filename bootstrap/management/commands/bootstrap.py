from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Bootstraps the environment with default development data'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(username='admin',
                                          email='admin@local',
                                          password='password')
            self.stdout.write(self.style.SUCCESS('Created admin superuser.'))