from rest_framework import generics, permissions
from rest_framework.response import Response
from dietitians.models import Dietitian
from .serializers import DietitianStatusUpdateSerializer
from rest_framework.permissions import IsAdminUser
from dietitians.serializers import DietitianSerializer


class UpdateDietitianStatusView(generics.UpdateAPIView):
    queryset = Dietitian.objects.all()
    serializer_class = DietitianStatusUpdateSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        dietitian = self.get_object()
        serializer = self.get_serializer(dietitian, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"success": f"Dietitian {dietitian.user.username} {'approved' if dietitian.status == 2 else 'rejected'}."})

        return Response(serializer.errors, status=400)

class DietitianDetailView(generics.RetrieveAPIView):
    queryset = Dietitian.objects.all()
    serializer_class = DietitianSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "id" 