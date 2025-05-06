from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create admin user'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='myadmin').exists():
            User.objects.create_superuser('myadmin', 'admin@example.com', 'StrongPassword123')
            print("Admin user created.")
        else:
            print("Admin user already exists.")