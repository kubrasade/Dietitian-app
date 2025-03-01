from rest_framework import serializers
from .models import Survey, SurveyFile

class SurveyFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyFile
        fields = ("id", "file")

class SurveySerializer(serializers.ModelSerializer):
    files = SurveyFileSerializer(many=True, required=False) 

    class Meta:
        model = Survey
        fields = "__all__"
        read_only_fields = ("id", "user")

    def create(self, validated_data):
        files_data = self.context["request"].FILES.getlist("files") 
        user = self.context["request"].user  
        validated_data["user"] = user  

        survey = Survey.objects.create(**validated_data)

        if len(files_data) > 5:
            raise serializers.ValidationError({"files": "You can upload a maximum of 5 files per survey."})

        file_instances = [SurveyFile(survey=survey, file=file) for file in files_data]
        SurveyFile.objects.bulk_create(file_instances)  

        return survey

    def update(self, instance, validated_data):
        files_data = self.context["request"].FILES.getlist("files")  
        instance = super().update(instance, validated_data)

        if instance.files.count() + len(files_data) > 5:
            raise serializers.ValidationError({"files": "You can upload a maximum of 5 files per survey."})

        file_instances = [SurveyFile(survey=instance, file=file) for file in files_data]
        SurveyFile.objects.bulk_create(file_instances)

        return instance