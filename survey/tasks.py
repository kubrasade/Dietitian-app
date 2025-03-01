from celery import shared_task
from datetime import timedelta
from django.utils.timezone import now
from .models import Survey

@shared_task
def delete_old_surveys():
    threshold_date = now() - timedelta(days=30)
    deleted_surveys = Survey.objects.filter(is_deleted=True, deleted_at__lte=threshold_date)
    
    count = deleted_surveys.count()
    deleted_surveys.delete()

    return f"{count} old surveys deleted."