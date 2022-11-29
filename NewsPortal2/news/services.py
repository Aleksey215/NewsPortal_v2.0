from django.template.loader import render_to_string
from datetime import datetime
from django.core.mail import EmailMultiAlternatives

from config.settings import DEFAULT_FROM_EMAIL
from .models import *
from .tasks import send_mail_task


def notify_subscribers(instance):
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
            send_mail_task.delay(subscriber_name, subscriber_email, html_content)


def weekly_emails_to_subscribers():
    categories = Category.objects.all()
    for category in categories:
        posts_for_category = []
        week_number_last = datetime.now().isocalendar()[1] - 1
        posts_list = Post.objects.filter(post_category_id=category.id, time_of_creation__week=week_number_last)
        for post in posts_list:
            posts_for_category.append(post)
        for subscriber in category.subscribers.all():
            name = subscriber.username
            email = subscriber.email
            html_content = render_to_string(
                'email/weekly_newsletter_mail.html', {
                    'username': name,
                    'category': category,
                    'posts': posts_list,
                }
            )
            msg = EmailMultiAlternatives(
                subject=f'Здравствуй, {name}. Новые статьи за прошлую неделю в вашем разделе!',
                from_email=DEFAULT_FROM_EMAIL,
                to=[email]
            )
            msg.attach_alternative(html_content, 'text/html')
            # msg.send()
            print(f'Category: {category.name}. Posts: {posts_list}. Subscriber: {subscriber.username}')
