from rest_framework import generics, permissions
from rest_framework.response import Response
from dietitians.models import Dietitian
from .serializers import DietitianStatusUpdateSerializer
from rest_framework.permissions import IsAdminUser
from dietitians.serializers import DietitianSerializer
from .services import DietitianStatusService, DietitianService, DietitianStatsService
from rest_framework.filters import SearchFilter

class UpdateDietitianStatusView(generics.UpdateAPIView):
    queryset = Dietitian.objects.all()
    serializer_class = DietitianStatusUpdateSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        dietitian = self.get_object()
        serializer = self.get_serializer(dietitian, data=request.data, partial=True)

        if serializer.is_valid():
            updated_dietitian = DietitianStatusService.update_dietitian_status(dietitian, serializer.validated_data['status'])

            return Response({
                "success": f"Dietitian {updated_dietitian.user.username} {'approved' if updated_dietitian.status == 2 else 'rejected'}."
            })

        return Response(serializer.errors, status=400)
    

class DietitianListView(generics.ListAPIView):
    serializer_class = DietitianSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter]
    search_fields = ['user__username', 'user__email']

    def get_queryset(self):
        return DietitianService.filter_dietitians(self.request.query_params)

class DietitianDetailView(generics.RetrieveAPIView):
    queryset = Dietitian.objects.all()
    serializer_class = DietitianSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "id" 

class DietitianStatsView(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        stats = DietitianStatsService.get_dietitian_statistics()
        return Response(stats)