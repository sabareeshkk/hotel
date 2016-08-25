"""
WSGI config for hotel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# setting file used in production mode(applies with gunicorn)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.base")

application = get_wsgi_application()
