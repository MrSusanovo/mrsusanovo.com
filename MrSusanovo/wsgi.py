"""
WSGI config for MrSusanovo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys

# try to solve "core.wsgi does not exist"

# add virtual environment path
sys.path.append('/usr/local/django/Susanovo/lib/python2.7/site-packages')

# add project path
sys.path.append('/usr/local/django/Susanovo/Personal/mrsusanovo.com/Mrsusanovo')

from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"] = "MrSusanovo.settings"

application = get_wsgi_application()
