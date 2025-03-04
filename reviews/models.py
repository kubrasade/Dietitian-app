from django.db import models
from django.conf import settings
from dietitians.models import Dietitian  
from core.enum import Status
from core.models import BaseModel

class Review(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dietitian = models.ForeignKey(Dietitian, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField(default=1)  
    comment = models.TextField(blank=True, null=True)
    status= models.PositiveSmallIntegerField(choices=Status.choices, default=Status.PENDING)

    class Meta:
        unique_together = ["user", "dietitian"]  

    def __str__(self):
        return f"{self.user.username} -> {self.dietitian.user.username} ({self.rating}/5)"