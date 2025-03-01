from django.urls import path
from .views import SurveyListCreateView, SurveyDetailView, BMICalculateView

urlpatterns = [
    path("surveys/", SurveyListCreateView.as_view(), name="survey-list"),
    path("<uuid:pk>/", SurveyDetailView.as_view(), name="survey-detail"),
    path('bmi/', BMICalculateView.as_view(), name='bmi-calculate'),

]