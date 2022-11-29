from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from datetime import datetime

from .models import *
from .services import notify_subscribers


@receiver(signal=m2m_changed, sender=PostCategory)
def new_post_send_mail(sender, instance, **kwargs):
    notify_subscribers(instance)
