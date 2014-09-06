"""
WSGI config for Tennis_Python project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Tennis_Python.settings")

app_apth = "/var/www/python_sites/Tennis_Python/"
sys.path.append(app_apth)
application = get_wsgi_application()
