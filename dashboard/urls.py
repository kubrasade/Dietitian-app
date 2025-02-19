from django.urls import path
from .views import (
    UpdateDietitianStatusView,
    DietitianDetailView
)

urlpatterns = [
    path('dietitian/status', UpdateDietitianStatusView.as_view(), name='update_dietitian_status'),
    path("dietitian/<int:id>/", DietitianDetailView.as_view(), name="dietitian-detail"),
]