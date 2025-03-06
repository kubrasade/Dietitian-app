from django.db import models
from django.conf import settings
from core.enum import Status
from core.models import BaseModel

class Match(BaseModel):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dietitian=models.ForeignKey('dietitians.Dietitian', on_delete=models.CASCADE, related_name="matches")
    status=models.PositiveSmallIntegerField(choices=Status.choices, default=Status.PENDING)

    class Meta:
        unique_together = ["user", "dietitian"]
        verbose_name = "Match"
        verbose_name_plural = "Matches"
        
    def __str__(self):
        return f"Match between {self.user.username} and {self.dietitian.user.username}"