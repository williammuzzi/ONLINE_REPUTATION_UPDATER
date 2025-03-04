import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ONLINE_REPUTATION_UPDATER.settings")

application = get_wsgi_application()
