import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.domain.entities.models.barbershop import Barbershop, Service

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Barbershop)
def log_barbershop_update(sender, instance, created, **kwargs):
    if created:
        logger.info(f"New barbershop created: {instance.name}")
    else:
        logger.info(f"Barbershop updated: {instance.name}")

@receiver(post_save, sender=Service)
def log_service_update(sender, instance, created, **kwargs):
    if created:
        logger.info(f"New service created: {instance.title}")
    else:
        logger.info(f"Service updated: {instance.title}")
