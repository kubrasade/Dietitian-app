from django.db import models

class UserRole(models.IntegerChoices):
    USER = 1, "User"
    DIETITIAN = 2, "Dietitian"    