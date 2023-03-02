from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class PresentationModel(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    result = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return self.title
