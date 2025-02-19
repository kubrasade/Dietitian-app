from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password
from .enum import UserRole
from dietitians.models import Dietitian

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password', 'password_confirmation', 'phone_number']
        extra_kwargs = {
            'phone_number': {'required': False, 'allow_null': True},  
        }

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError({"password_confirmation": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation')  

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number', None),  
            role=UserRole.USER
        )

        return user

class DietitianRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=8)  
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = Dietitian
        fields = '__all__'  
        extra_kwargs = {
            'user': {'required': False}  
        }
        
    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError({"password_confirmation": "Passwords do not match."})
        return data

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        validated_data.pop('password_confirmation') 

        user = User.objects.create_user(
            username=email,  
            email=email,
            password=password, 
            role=UserRole.DIETITIAN  
        )

        dietitian = Dietitian.objects.create(
            user=user,
            **validated_data
        )

        return dietitian
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError("Incorrect username or password.")

        if not user.is_active:
            raise serializers.ValidationError("This account is inactive.")

        data["user"] = user
        return data
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, min_length=8)

    def validate_old_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError("Incorrect old password.")
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance