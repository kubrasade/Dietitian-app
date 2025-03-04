from rest_framework import generics, permissions
from .models import Dietitian
from .serializers import  DietitianSerializer, DietitianDetailSerializer

class DietitianListView(generics.ListAPIView):
    queryset = Dietitian.objects.all()
    serializer_class = DietitianSerializer
    permission_classes = [permissions.AllowAny]

class DietitianDetailView(generics.RetrieveAPIView):
    queryset = Dietitian.objects.all()
    serializer_class = DietitianDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
