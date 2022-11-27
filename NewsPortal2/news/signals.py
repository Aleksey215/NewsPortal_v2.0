from django.db.models.signals import m2m_changed
# декоратор для подключения функции к нужному сигналу
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import *
from .tasks import send_mail_subscribers_task



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
            send_mail_subscribers_task.delay(subscriber_name, subscriber_email, html_content)
