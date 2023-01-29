from django.db import models
from django.utils import timezone


class BaseModel(models.Model):  # type: ignore
    class Meta:
        abstract = True

    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
