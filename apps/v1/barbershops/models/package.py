from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from apps.v1.shared.models import BaseModel


class Package(BaseModel, TranslatableModel):
    price = models.IntegerField(
        verbose_name=_("Price"),
        help_text=_("The price of the package"),
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to="packages/",
        unique=True,
        help_text=_("The image representing the package"),
    )
    service = models.ForeignKey(
        "barbershops.Service",
        on_delete=models.CASCADE,
        related_name="packages",
        verbose_name=_("Service"),
        help_text=_("The service this package belongs to"),
    )

    translations = TranslatedFields(
        name=models.CharField(
            verbose_name=_("Name"),
            max_length=255,
            unique=True,
            help_text=_("The name of the package"),
        ),
    )

    class Meta:
        ordering = ["created"]
        verbose_name = _("Package")
        verbose_name_plural = _("Packages")

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True)
