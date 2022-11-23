# для получения сигнала о создании нового объекта
import time

from django.db.models.signals import post_save
# декоратор для подключения функции к нужному сигналу
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from time import sleep

from .models import *


@receiver(signal=post_save, sender=Post)
def notify_subscribers(sender, instance, created, **kwargs):
        categories = Category.objects.filter(post__id=instance.id)
        print(categories)
        print(Category.objects.get(pk=Post.objects.get(pk=instance.id).category.all([])))

