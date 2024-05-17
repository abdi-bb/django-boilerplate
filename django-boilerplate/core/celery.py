import os

from decouple import config
from celery import Celery

if config('DEBUG', default=False, cast=bool):
    django_settings_module = config("DJANGO_SETTINGS_MODULE_DEV")
else:
    django_settings_module = config("DJANGO_SETTINGS_MODULE_PROD")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings_module)

app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()