from django.core.exceptions import ValidationError
from django.db import models

from config.settings.base import AUTH_USER_MODEL
from .review import Review
from ..shared import BaseModel

class ReviewLike(BaseModel):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='liked_reviews')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes')

    def clean(self):
        super().clean()
        if hasattr(self, 'user') and hasattr(self, 'review') and self.user and self.review:
            if ReviewLike.objects.filter(user=self.user, review=self.review).exclude(pk=self.pk).exists():
                raise ValidationError("You have already liked this review.")

    class Meta:
        unique_together = ('user', 'review')

    def __str__(self):
        return f"{self.user} liked review {self.review.id}"