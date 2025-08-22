from django.db import models

from domain.entities.models.shared import BaseModel


class Specialty(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = "infrastructure"