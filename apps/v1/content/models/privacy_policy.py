from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from apps.v1.shared.models import BaseModel


class PrivacyPolicy(BaseModel, TranslatableModel):
    display_order = models.SmallIntegerField(
        verbose_name=_("Display Order"),
        default=1,
        help_text=_("The order in which the privacy policy is displayed"),
    )

    translations = TranslatedFields(
        title=models.CharField(
            verbose_name=_("Title"),
            max_length=255,
            unique=True,
            help_text=_("The title of the privacy policy"),
        ),
        description=models.TextField(
            verbose_name=_("Description"),
            unique=True,
            help_text=_("The description of the privacy policy"),
        ),
    )

    class Meta:
        ordering = ["display_order", "created"]
        verbose_name = _("Privacy Policy")
        verbose_name_plural = _("Privacy Policies")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)
