from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from apps.v1.shared.models import BaseModel


class Barbershop(BaseModel, TranslatableModel):
    owner = models.ForeignKey(
        to="accounts.Profile",
        on_delete=models.CASCADE,
        related_name="barbershops",
        verbose_name=_("Owner"),
        help_text=_("The profile that owns the barbershop"),
    )
    address = models.ForeignKey(
        to="shared.Address",
        on_delete=models.CASCADE,
        related_name="barbershops",
        verbose_name=_("Address"),
        help_text=_("The address of the barbershop"),
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to="barbershops/",
        unique=True,
        help_text=_("The image representing the barbershop"),
    )
    rating = models.SmallIntegerField(
        verbose_name=_("Rating"),
        default=0,
        help_text=_("The average rating of the barbershop"),
    )

    translations = TranslatedFields(
        title=models.CharField(
            verbose_name=_("Title"),
            max_length=255,
            unique=True,
            help_text=_("The title of the barbershop"),
        ),
        description=models.TextField(
            verbose_name=_("Description"),
            unique=True,
            help_text=_("The description of the barbershop"),
        ),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Barbershop")
        verbose_name_plural = _("Barbershops")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)
