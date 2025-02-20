from dietitians.models import Dietitian
from django.db.models import Q
from datetime import datetime,timedelta
from django.utils.timezone import make_aware, now
from core.enum import Status

class DietitianStatusService:
    @staticmethod
    def update_dietitian_status(dietitian, status):
        dietitian.status = status

        dietitian.is_active = True if status == 2 else False
        dietitian.save()

        return dietitian
    