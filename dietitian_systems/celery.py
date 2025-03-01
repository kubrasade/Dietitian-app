from celery.schedules import crontab
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dietitian_systems.settings")

app = Celery("dietitian_systems")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "delete-old-records-every-day": {
        "task": "document.tasks.delete_old_records",
        "schedule": crontab(hour=0, minute=0), 
    },   
}

app.autodiscover_tasks()