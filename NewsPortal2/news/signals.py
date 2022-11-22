# для получения сигнала о создании нового объекта
from django.db.models.signals import post_save
# декоратор для подключения функции к нужному сигналу
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives

from models import Post


@receiver(signal=post_save, sender=Post)
def notify_subscribers(sender, instance, created, **kwargs):
    if created:
        recipients_emails = []
        post_categories = instance.category.all()
        for category in post_categories:
            for subscriber in category.subscribers.all():
                recipients_emails.append(subscriber.email)
        print(recipients_emails)
