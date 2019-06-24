"""
WSGI config for rango_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

path = 'C:/Users/ASUS1/AppData/Local/Packages/CanonicalGroupLimited.Ubuntu18.04onWindows_79rhkp1fndgsc/LocalState/rootfs/home/asus1/rango_project'
if path not in sys.path:
    sys.path.append(path)

os.chdir(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rango_project.settings')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
