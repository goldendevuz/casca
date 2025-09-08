from django.db import models


class DiscountTypes(models.TextChoices):
    PERCENT = "percent", "Percent"
    AMOUNT = "amount", "Amount"

    def __str__(self):
        return self.label


class NotificationStates(models.TextChoices):
    NEW = "new", "New"
    READ = "read", "Read"

    def __str__(self):
        return self.label


class UserRoles(models.TextChoices):
    ORDINARY_USER = "ordinary_user", "Ordinary User"
    CUSTOMER = "customer", "Customer"
    BARBER = "barber", "Barber"
    MANAGER = "manager", "Manager"
    ADMIN = "admin", "Admin"
    SUPER_ADMIN = "super_admin", "Super Admin"

    def __str__(self):
        return self.label


class Genders(models.TextChoices):
    MALE = "male", "Male"
    FEMALE = "female", "Female"

    def __str__(self):
        return self.label


class AuthStatuses(models.TextChoices):
    NEW = "new", "New"
    CODE_VERIFIED = "code_verified", "Code Verified"
    DONE = "done", "Done"

    def __str__(self):
        return self.label


class AuthTypes(models.TextChoices):
    VIA_PHONE = "via_phone", "Via Phone"
    VIA_EMAIL = "via_email", "Via Email"

    def __str__(self):
        return self.label


class Themes(models.TextChoices):
    SYSTEM = "system", "System"
    LIGHT = "light", "Light"
    DARK = "dark", "Dark"

    def __str__(self):
        return self.label


class PaymentStatuses(models.TextChoices):
    PENDING = "pending", "Pending"
    PAID = "paid", "Paid"
    FAILED = "failed", "Failed"
    REFUNDED = "refunded", "Refunded"

    def __str__(self):
        return self.label


class AppointmentStatuses(models.TextChoices):
    PENDING = "pending", "Pending"
    SCHEDULED = "scheduled", "Scheduled"
    CANCELED = "canceled", "Canceled"
    RESCHEDULED = "rescheduled", "Rescheduled"
    APPROVED = "approved", "Approved"
    ONGOING = "ongoing", "Ongoing"
    COMPLETED = "completed", "Completed"
    REFUNDED = "refunded", "Refunded"

    def __str__(self):
        return self.label


class ReasonTypes(models.TextChoices):
    CHANGE_IN_PLANS = "change_in_plans", "Change in Plans"
    UNABLE_TO_CONTACT_BARBER = "unable_to_contact_barber", "Unable to Contact Barber"
    WRONG_ADDRESS_SHOWN = "wrong_address_shown", "Wrong Address Shown"
    THIS_PRICE_IS_NOT_REASONABLE = "this_price_is_not_reasonable", "This Price is Not Reasonable"
    BOOKING_MISTAKE = "booking_mistake", "Booking Mistake"
    POOR_WEATHER_CONDITIONS = "poor_weather_conditions", "Poor Weather Conditions"
    OTHER = "other", "Other"

    def __str__(self):
        return self.label
