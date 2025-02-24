from django.db import models 

class Activity_Level(models.IntegerChoices):
    SEDENTARY = 1, "Sedentary"
    LIGHT = 2, "Light"
    MODERATE = 3, "Moderate"
    ACTIVE = 4, "Active"
    VERY_ACTIVE = 5, "Very Active"

class Goals(models.IntegerChoices):
    WEIGHT_LOSS = 1, "Weight Loss"
    WEIGHT_GAIN = 2, "Weight Gain"
    MAINTAIN_WEIGHT = 3, "Maintain Weight"
    OTHER = 4, "Other"
    

