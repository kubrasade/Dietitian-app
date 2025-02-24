from rest_framework import generics, permissions, serializers
from .models import Survey, SurveyFile
from .serializers import SurveySerializer, SurveyFileSerializer

class SurveyListCreateView(generics.ListCreateAPIView):
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Survey.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SurveyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Survey.objects.filter(user=self.request.user)
    

class SurveyFileListCreateView(generics.ListCreateAPIView):
    serializer_class = SurveyFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SurveyFile.objects.filter(survey__user=self.request.user)

    def perform_create(self, serializer):
        survey_id = self.request.data.get("survey")
        survey = Survey.objects.filter(id=survey_id, user=self.request.user).first()
        if not survey:
            raise serializers.ValidationError({"survey": "Invalid or unauthorized survey."})
        
        if survey.files.count() >= 5:
            raise serializers.ValidationError({"files": "You can upload a maximum of 5 files per survey."})

        serializer.save(survey=survey)