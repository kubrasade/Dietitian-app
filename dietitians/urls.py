from django.urls import path
from .views import DietitianListView, DietitianDetailView

urlpatterns = [
    path("", DietitianListView.as_view(), name="dietitian-list"),
    path("<int:pk>/", DietitianDetailView.as_view(), name="dietitian-detail"),
]