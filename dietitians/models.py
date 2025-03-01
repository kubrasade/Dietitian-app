from django.db import models
from django.contrib.auth import get_user_model
from core.enum import Gender, Status
from core.models import BaseModel
from .enum import ExpertiseField
from django.core.validators import MinValueValidator


User= get_user_model()

def dietitian_directory_path(instance, filename):
    return f'dietitians/{instance.user.id}/{filename}'

class Dietitian(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="dietitian_profile")
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    title= models.CharField(max_length=100)
    licence_number = models.CharField(max_length=50, unique=True)
    diploma = models.FileField(upload_to=dietitian_directory_path, null=True, blank=True)
    experience_years = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    expertise_fields = models.PositiveSmallIntegerField(ExpertiseField, blank=True) 
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.PENDING)
    gender = models.PositiveSmallIntegerField(choices=Gender.choices) 
    location = models.CharField(max_length=255) 
    website = models.URLField(blank=True, null=True)  
    social_media = models.JSONField(blank=True, null=True)  
    references = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Dietitian"
        verbose_name_plural = "Dietitians"

    def save(self, *args, **kwargs):
        super(Dietitian, self).save(*args, **kwargs)

        if self.user and self.user.username != self.username:  
            self.user.username = self.username
            self.user.save(update_fields=["username"]) 

    def __str__(self):
        return f"{self.user.username} - {self.get_status_display()}"

class Certification(models.Model):
    dietitian = models.ForeignKey(Dietitian, on_delete=models.CASCADE, related_name="certifications")
    file = models.FileField(upload_to=dietitian_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Certification for {self.dietitian.user.username}"