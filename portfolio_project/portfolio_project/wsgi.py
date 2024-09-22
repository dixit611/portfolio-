"""
WSGI config for portfolio_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import environ

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

environ.Env.read_env()  # Load environment variables from .env file

# Debugging: Print environment variables
print(f"DB_NAME: {os.getenv('DB_NAME')}")
print(f"EMAIL_HOST_USER: {os.getenv('EMAIL_HOST_USER')}")

application = get_wsgi_application()

app = application
