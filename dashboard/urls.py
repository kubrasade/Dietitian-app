from django.urls import path
from .views import (
    UpdateDietitianStatusView,
)

urlpatterns = [
    path('dietitian/status/<int:pk>/', UpdateDietitianStatusView.as_view(), name='update_dietitian_status'),
]