from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import PostCategory
from .tasks import send_mail_task


@receiver(signal=m2m_changed, sender=PostCategory)
def new_post_send_mail(sender, instance, **kwargs):
    categories = instance.category.prefetch_related("subscribers").all()
    for category in categories:
        for subscriber in category.subscribers.all():
            subscriber_name = subscriber.username
            subscriber_email = subscriber.email
            html_content = render_to_string(
                'email/new_post_mail.html', {
                    'post': instance,
                    'content': instance.content[:50],
                }
            )
            send_mail_task.delay(subscriber_name, subscriber_email, html_content, weekly_task=False)
