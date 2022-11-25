from django.db.models.signals import m2m_changed
# декоратор для подключения функции к нужному сигналу
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import *
from config.settings import DEFAULT_FROM_EMAIL


@receiver(signal=m2m_changed, sender=PostCategory)
def notify_subscribers(sender, instance, **kwargs):
    post_categories = Category.objects.prefetch_related("subscribers").filter(post=instance)
    for category in post_categories:
        for subscriber in category.subscribers.all():
            subscriber_name = subscriber.username
            subscriber_email = subscriber.email
            html_content = render_to_string(
                'email/new_post_mail.html',{
                    'post': instance,
                    'content': instance.content[:50],
                }
            )
            msg = EmailMultiAlternatives(
                subject=f'Здравствуй, {subscriber_name}. Новая статья в вашем разделе!',
                from_email=DEFAULT_FROM_EMAIL,
                to=[subscriber_email]
            )
            msg.attach_alternative(html_content, 'text/html')
            msg.send()
