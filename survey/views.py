from rest_framework import generics, permissions, serializers
from .models import Survey, SurveyFile
from .serializers import SurveySerializer, SurveyFileSerializer
from core.mixins import BaseMixin

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

