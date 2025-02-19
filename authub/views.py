from django.contrib.auth import get_user_model
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import (
    UserRegistrationSerializer, 
    DietitianRegistrationSerializer, 
    LoginSerializer, 
)
from .services import authenticate_user, reset_password
from rest_framework_simplejwt.tokens import RefreshToken



User = get_user_model()


class UserRegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class DietitianRegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = DietitianRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        response_data = authenticate_user(data.get("username"), data.get("password"))
        return Response(response_data, status=status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response({"error": "Refresh token not found."}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetConfirmView(APIView):
    def post(self, request, uidb64, token):
        new_password = request.data.get("new_password")
        response_data = reset_password(uidb64, token, new_password)
        return Response(response_data, status=status.HTTP_200_OK)