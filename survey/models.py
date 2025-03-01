import uuid
import os
from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import BaseModel  
from core.enum import Gender
from .enum import Activity_Level, Goals
from django.core.validators import FileExtensionValidator

User = get_user_model()

def validate_file(value):
    allowed_extensions = ['.pdf', '.jpg', '.jpeg', '.png']  
    max_file_size = 10 * 1024 * 1024  

    file_name, file_extension = os.path.splitext(value.name)
    
    if file_extension.lower() not in allowed_extensions:
        raise ValidationError(f"Only {', '.join(allowed_extensions)} files are allowed.")

    if value.size > max_file_size:
        raise ValidationError("File size should not exceed 10 MB.")

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}" 
    return os.path.join(f"user_{instance.survey.user.id}/survey_files", filename)

class Survey(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="survey"
    )
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(80)]
    )
    gender = models.PositiveSmallIntegerField(choices=Gender.choices)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    medical_conditions = models.TextField(blank=True, null=True)
    dietary_restrictions = models.TextField(blank=True, null=True)
    medications = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    sleep_hours = models.PositiveIntegerField(
        blank=True, null=True,
        validators=[MinValueValidator(0), MaxValueValidator(24)]
    )
    stress_level = models.PositiveIntegerField(
        blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    activity_level = models.PositiveSmallIntegerField(choices=Activity_Level.choices)
    smoking = models.BooleanField(default=False)
    alcohol_use = models.BooleanField(default=False)
    water_intake = models.PositiveIntegerField(
        blank=True, null=True,
        validators=[MinValueValidator(0), MaxValueValidator(5000)]
    )
    goals = models.PositiveSmallIntegerField(choices=Goals.choices)
    target_weight = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    motivation_level = models.PositiveIntegerField(
        blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    eating_disorders = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Survey for {self.user.username}"

    class Meta:
        verbose_name = "Survey"
        verbose_name_plural = "Surveys"

    def clean(self):
        if self.target_weight and self.target_weight >= self.weight:
            raise ValidationError({"target_weight": "The target weight should be less than the current weight."})

class SurveyFile(BaseModel):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to=user_directory_path, validators=[validate_file])

    class Meta:
        unique_together = ('survey', 'file')
        verbose_name = "Survey File"
        verbose_name_plural = "Survey Files"

    def clean(self):
        if self.survey.files.count() >= 5:
            raise ValidationError("You can upload a maximum of 5 files per survey.")

    def delete(self, *args, **kwargs):
        if self.file and self.file.storage.exists(self.file.name):
            self.file.delete(save=False)  

        super(SurveyFile, self).delete(*args, **kwargs)  

    def __str__(self):
        return f"File for {self.survey.user.username}"