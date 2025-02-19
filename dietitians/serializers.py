from rest_framework import serializers
from dietitians.models import Dietitian
from core.enum import Status

class DietitianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dietitian
        fields = "__all__"