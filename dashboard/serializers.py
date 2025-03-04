from rest_framework import serializers
from dietitians.models import Dietitian
from core.enum import Status
from reviews.models import Review

class DietitianStatusUpdateSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Status.choices)

    class Meta:
        model = Dietitian
        fields = ['status']

    def validate_status(self, value):
        if value not in [Status.APPROVED, Status.REJECTED]:
            raise serializers.ValidationError("Invalid status. Allowed values: 2 (Approved), 3 (Rejected).")
        return value
    
class ReviewAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "user", "dietitian", "rating", "comment", "status", "created_at"]

class ReviewStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Status.choices)