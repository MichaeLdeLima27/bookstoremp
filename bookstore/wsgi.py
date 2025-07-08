"""
WSGI config for bookstore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import sys
import os

path = "/home/Michaelmp/bookstoremp"
if path not in sys.path:
    sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"] = "bookstoremp.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
