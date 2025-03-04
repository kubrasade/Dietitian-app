from django.urls import path
from .views import (
    UpdateDietitianStatusView,
    DietitianDetailView,
    DietitianListView,
    DietitianStatsView,
    AdminReviewListView, 
    AdminReviewStatusUpdateView
)

urlpatterns = [
    path('dietitian/status/<int:pk>/', UpdateDietitianStatusView.as_view(), name='update_dietitian_status'),
    path("dietitian/<int:id>/", DietitianDetailView.as_view(), name="dietitian-detail"),
    path('dietitians/', DietitianListView.as_view(), name='dietitian-list'),
    path('dietitian/stats/', DietitianStatsView.as_view(), name='dietitian-stats'),
    path("reviews/pending/", AdminReviewListView.as_view(), name="admin-review-list"),
    path("reviews/<int:pk>/status/", AdminReviewStatusUpdateView.as_view(), name="admin-review-status"),
]