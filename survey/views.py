from rest_framework import generics, permissions, serializers
from .models import Survey
from .serializers import SurveySerializer,BMISerializer
from core.mixins import BaseMixin
from rest_framework.response import Response
from .services import SurveyService
from rest_framework.views import APIView



class SurveyListCreateView(BaseMixin, generics.ListCreateAPIView):
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAuthenticated]
    model= Survey

    def perform_create(self, serializer):
        existing_survey = Survey.objects.filter(user= self.request.user, is_deleted= True).first()
        if existing_survey:
            existing_survey.is_deleted = False
            existing_survey.save()
        else:
            serializer.save(user=self.request.user)

class SurveyDetailView(BaseMixin,generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAuthenticated]
    model= Survey

class BMICalculateView(BaseMixin, APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BMISerializer

    def get(self, request, *args, **kwargs):
        survey = Survey.objects.filter(user=request.user).first()
        if not survey:
            return Response({"error": "Survey not found."}, status=404)

        bmi_result = SurveyService.calculate_bmi(survey.weight, survey.height)
        return Response(bmi_result, status=200)

