from django.urls import path
from .views import (
    UpdateDietitianStatusView,
    DietitianDetailView,
    DietitianListView,
    DietitianStatsView
)

urlpatterns = [
    path('dietitian/status/<int:pk>/', UpdateDietitianStatusView.as_view(), name='update_dietitian_status'),
    path("dietitian/<int:id>/", DietitianDetailView.as_view(), name="dietitian-detail"),
    path('dietitians/', DietitianListView.as_view(), name='dietitian-list'),
    path('dietitian/stats/', DietitianStatsView.as_view(), name='dietitian-stats'),

]