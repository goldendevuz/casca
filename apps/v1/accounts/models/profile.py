from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.v1.shared.models import BaseModel
from apps.v1.shared.enums import Themes, Genders, UserRoles


class Profile(BaseModel):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name=_("User"),
        help_text=_("The user account associated with this profile"),
    )
    is_location_enabled = models.BooleanField(
        verbose_name=_("Location Enabled"),
        default=False,
        help_text=_("Whether the user has enabled location tracking"),
    )
    avatar = models.ImageField(
        verbose_name=_("Avatar"),
        upload_to="avatars/",
        blank=True,
        null=True,
        help_text=_("The profile avatar image"),
    )
    theme = models.CharField(
        verbose_name=_("Theme"),
        max_length=20,
        choices=Themes.choices,
        default=Themes.SYSTEM,
        help_text=_("The theme preference for the app"),
    )
    app_language = models.ForeignKey(
        "languages.Language",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="profiles",
        verbose_name=_("App Language"),
        help_text=_("Preferred app language"),
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        max_length=10,
        choices=Genders.choices,
        blank=True,
        null=True,
        help_text=_("Gender of the user"),
    )
    birth_date = models.DateField(
        verbose_name=_("Birth Date"),
        blank=True,
        null=True,
    )
    full_name = models.CharField(
        verbose_name=_("Full Name"),
        max_length=150,
        blank=True,
        null=True,
        unique=True,
        help_text=_("Full name of the user"),
    )
    role = models.CharField(
        verbose_name=_("Role"),
        max_length=20,
        choices=UserRoles.choices,
        default=UserRoles.CUSTOMER,
        help_text=_("The role of the user"),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.full_name or str(self.user)
