from rest_framework import serializers
from .models import Review

class BaseReviewSerializer(serializers.ModelSerializer):    
    def validate_rating(self, value):
        if not isinstance(value, int):
            raise serializers.ValidationError("Rating must be an integer between 1 and 10.")
        if value < 1 or value > 10:
            raise serializers.ValidationError("Rating must be between 1 and 10.")
        return value

class ReviewSerializer(BaseReviewSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ["id", "user", "dietitian", "rating", "comment", "status", "created_at"]
        read_only_fields = ["id", "user", "created_at", "status"]

class ReviewUpdateSerializer(BaseReviewSerializer):
    class Meta:
        model = Review
        fields = ["rating", "comment"]

class ReviewDeleteSerializer(serializers.Serializer):
    review_id = serializers.IntegerField()