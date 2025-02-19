from django.db import models
from core.mixins import BaseModel
from django.contrib.auth.models import AbstractUser
from .enum import UserRole


class User(BaseModel,AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    dietitian = models.ForeignKey(
        'dietitians.Dietitian',
        on_delete=models.SET_NULL,  
        related_name='clients',
        blank=True,
        null=True,
    )
    role = models.PositiveSmallIntegerField(choices=UserRole.choices, default=UserRole.USER)
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"