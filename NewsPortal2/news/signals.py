# для получения сигнала о создании нового объекта
import time

from django.db.models.signals import post_save, m2m_changed
# декоратор для подключения функции к нужному сигналу
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from time import sleep

from .models import *


@receiver(signal=m2m_changed, sender=PostCategory)
def notify_subscribers(sender, instance, **kwargs):
    recipients = []
    categories = instance.category.all()
    for category in categories:
        print(category.subscribers.all().email)

