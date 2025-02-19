from django.db import models

class ExpertiseField(models.IntegerChoices):
    GENERAL = 1, "General"
    WEIGHT_MANAGEMENT = 2, "Weight Management"
    SPORTS_NUTRITION = 3, "Sports Nutrition"
    DIABETIC_DIET = 4, "Diabetic Diet"
    PREGNANCY_NUTRITION = 5, "Pregnancy Nutrition"
    CHILD_NUTRITION = 6, "Child Nutrition"
    VEGAN_DIET = 7, "Vegan Diet"
    FOOD_ALLERGY = 8, "Food Allergy"
    BARIATRIC_NUTRITION = 9, "Bariatric Nutrition"
    CANCER_NUTRITION = 10, "Cancer Nutrition"
    CARDIO_NUTRITION = 11, "Cardio Nutrition"
    CLINICAL_DIET = 12, "Clinical Diet"
    EATING_DISORDERS = 13, "Eating Disorders"
