from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import ReviewSerializer, ReviewUpdateSerializer, ReviewDeleteSerializer
from .services import ReviewService
from core.permissions import IsOwner

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.instance = ReviewService.create_review(self.request.user, serializer.validated_data)

class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return ReviewService.get_approved_reviews()

class ReviewUpdateView(generics.UpdateAPIView):
    serializer_class = ReviewUpdateSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwner]

    def update(self, request, *args, **kwargs):
        review_id = self.kwargs.get("pk")
        updated_review = ReviewService.update_review(request.user, review_id, request.data)
        return Response(ReviewSerializer(updated_review).data, status=status.HTTP_200_OK)

class ReviewDeleteView(generics.DestroyAPIView):
    serializer_class = ReviewDeleteSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwner]

    def destroy(self, request, *args, **kwargs):
        serializer = ReviewDeleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review_id = serializer.validated_data["review_id"]

        ReviewService.delete_review(request.user, review_id)
        return Response({"message": "Review deleted successfully."}, status=status.HTTP_204_NO_CONTENT)