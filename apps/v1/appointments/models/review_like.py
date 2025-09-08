from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.v1.shared.models import BaseModel


class ReviewLike(BaseModel):
    profile = models.ForeignKey(
        "accounts.Profile",
        on_delete=models.CASCADE,
        related_name="review_likes",
        verbose_name=_("Profile"),
        help_text=_("The profile that liked the review"),
    )
    review = models.ForeignKey(
        "reviews.Review",
        on_delete=models.CASCADE,
        related_name="likes",
        verbose_name=_("Review"),
        help_text=_("The review that was liked"),
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["profile", "review"],
                name="unique_review_like",
            )
        ]
        ordering = ["-created"]
        verbose_name = _("Review Like")
        verbose_name_plural = _("Review Likes")

    def __str__(self):
        return f"{self.profile} → {self.review}"
