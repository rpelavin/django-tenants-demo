from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Bootstraps the environment with default development data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('TODO: boostrap here'))