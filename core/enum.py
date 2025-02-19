from django.db import models 

class Gender(models.IntegerChoices):
    MALE = 1, "Male"
    FEMALE = 2, "Female"
    OTHER = 3, "Other"

class Status(models.IntegerChoices):
    PENDING= 1, "Pending"
    APPROVED= 2, "Approved"
    REJECTED= 3, "Rejected"