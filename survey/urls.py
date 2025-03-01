from django.urls import path
from .views import SurveyListCreateView, SurveyDetailView

urlpatterns = [
    path("surveys/", SurveyListCreateView.as_view(), name="survey-list"),
    path("<uuid:pk>/", SurveyDetailView.as_view(), name="survey-detail"),
]