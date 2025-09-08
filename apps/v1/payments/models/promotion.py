from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from apps.v1.shared.models import BaseModel
from apps.v1.shared.enums import DiscountTypes


class Promotion(BaseModel, TranslatableModel):
    code = models.CharField(
        verbose_name=_("Code"),
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        help_text=_("The unique code for the promotion"),
    )
    discount_type = models.CharField(
        verbose_name=_("Discount Type"),
        max_length=10,
        choices=DiscountTypes.choices,
        default=DiscountTypes.PERCENT,
        help_text=_("The type of discount applied"),
    )
    discount_value = models.IntegerField(
        verbose_name=_("Discount Value"),
        help_text=_("The value of the discount"),
    )
    valid_to = models.DateTimeField(
        verbose_name=_("Valid To"),
        blank=True,
        null=True,
        help_text=_("The expiry date of the promotion"),
    )
    minimum_spend = models.IntegerField(
        verbose_name=_("Minimum Spend"),
        blank=True,
        null=True,
        help_text=_("Minimum spend required to apply this promotion"),
    )
    usage_limit = models.SmallIntegerField(
        verbose_name=_("Usage Limit"),
        blank=True,
        null=True,
        help_text=_("Maximum number of times this promotion can be used"),
    )
    used_count = models.SmallIntegerField(
        verbose_name=_("Used Count"),
        default=0,
        help_text=_("Number of times the promotion has been used"),
    )
    display_order = models.SmallIntegerField(
        verbose_name=_("Display Order"),
        default=1,
        help_text=_("Order in which the promotion is displayed"),
    )

    translations = TranslatedFields(
        title=models.CharField(
            verbose_name=_("Title"),
            max_length=100,
            help_text=_("The title of the promotion"),
        ),
        description=models.TextField(
            verbose_name=_("Description"),
            blank=True,
            null=True,
            help_text=_("Optional description of the promotion"),
        ),
    )

    class Meta:
        ordering = ["display_order", "-created"]
        verbose_name = _("Promotion")
        verbose_name_plural = _("Promotions")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)
