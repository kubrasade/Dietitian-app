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
    
class DietitianService:
    @staticmethod
    def filter_dietitians(query_params):
        queryset = Dietitian.objects.all()

        status = query_params.get('status')
        is_active = query_params.get('is_active')
        start_date = query_params.get('start_date')
        end_date = query_params.get('end_date')
        search = query_params.get('search')

        if status is not None:
            queryset = queryset.filter(status=status)

        if is_active is not None:
            queryset = queryset.filter(is_active=is_active)

        if start_date and end_date:
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
                end_date = datetime.strptime(end_date, "%Y-%m-%d")
                start_date = make_aware(start_date)
                end_date = make_aware(end_date)

                queryset = queryset.filter(created_at__range=[start_date, end_date])
            except ValueError:
                pass 

        if search:
            queryset = queryset.filter(
                Q(user__username__icontains=search) |
                Q(user__email__icontains=search) |
                Q(user__first_name__icontains=search) |
                Q(user__last_name__icontains=search) |
                Q(title__icontains=search)  
            )

        return queryset
    
class DietitianStatsService:
    @staticmethod
    def get_dietitian_statistics():
        today = now()
        last_30_days = today - timedelta(days=30)

        stats = {
            "total_dietitians": Dietitian.objects.count(),
            "approved_dietitians": Dietitian.objects.filter(status=Status.APPROVED).count(),
            "pending_dietitians": Dietitian.objects.filter(status=Status.PENDING).count(),
            "rejected_dietitians": Dietitian.objects.filter(status=Status.REJECTED).count(),
            "last_30_days_applications": Dietitian.objects.filter(created_at__gte=last_30_days).count(),
            "active_dietitians": Dietitian.objects.filter(is_active=True).count(),
        }

        return stats