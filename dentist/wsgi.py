"""
WSGI config for dentist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.auth import get_user_model
from django.core.management import call_command

User = get_user_model()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dentist.settings')

application = get_wsgi_application()
# from django.core.management import call_command
# call_command('createadmin')

def create_admin_if_needed():
    if not User.objects.filter(is_superuser=True).exists():
        call_command('createadmin')
