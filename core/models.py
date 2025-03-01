from django.db import models
from django.utils.timezone import now

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at= now()
        self.save()

    class Meta:
        abstract = True

class BaseModel(TimeStampedModel, SoftDeleteModel):
    class Meta:
        abstract = True