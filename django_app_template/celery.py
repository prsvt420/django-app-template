import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app_template.settings")

app = Celery("django_app_template")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
