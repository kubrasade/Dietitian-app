from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from .models import Review
from core.enum import Status
from dietitians.models import Dietitian

class ReviewService:
    @staticmethod
    def create_review(user, data):
        dietitian_id = data.get("dietitian")
        Review.objects.filter(user=user, dietitian_id=dietitian_id).delete()
        return Review.objects.create(user=user, **data)
    
    @staticmethod
    def get_approved_reviews():
        return Review.objects.filter(status=Status.APPROVED)

    @staticmethod
    def get_dietitian_reviews(dietitian_id):
        return Review.objects.filter(dietitian_id=dietitian_id, status=Status.APPROVED)

    @staticmethod
    def update_review(user, review_id, data):
        review = get_object_or_404(Review, id=review_id, user=user)

        if "dietitian" in data:  
            dietitian_id = data.pop("dietitian")
            data["dietitian"] = get_object_or_404(Dietitian, id=dietitian_id)

        for key, value in data.items():
            setattr(review, key, value)

        review.save()  
        return review

    @staticmethod
    def delete_review(user, review_id):
        review = get_object_or_404(Review, id=review_id, user=user)
        review.delete()
        return True