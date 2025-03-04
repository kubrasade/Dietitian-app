from django.urls import path
from .views import ReviewCreateView, ReviewListView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path("add/", ReviewCreateView.as_view(), name="review-create"),
    path("dietitians/<int:dietitian_id>/", ReviewListView.as_view(), name="review-list"),
    path("<int:pk>/edit/", ReviewUpdateView.as_view(), name="review-update"),
    path("delete/", ReviewDeleteView.as_view(), name="review-delete"),
]