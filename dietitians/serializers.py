from rest_framework import serializers
from dietitians.models import Dietitian
from core.enum import Status

class DietitianSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Dietitian
        fields = ["first_name","last_name","image","average_rating","expertise_field"]
        
    def get_average_rating(self, obj):
        return obj.average_rating()

class DietitianDetailSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Dietitian
        fields = "__all__"
        
    def get_average_rating(self, obj):
        return obj.average_rating()