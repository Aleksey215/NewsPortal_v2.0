from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import datetime

from config.settings import DEFAULT_FROM_EMAIL
from .models import *


@shared_task
def send_mail_task(subscriber_name, subscriber_email, html_content, weekly_task):
    if not weekly_task:
        print('*** Task to send an email to a subscriber ***')
        msg = EmailMultiAlternatives(
            subject=f'Здравствуй, {subscriber_name}. Новая статья в вашем разделе!',
            from_email=DEFAULT_FROM_EMAIL,
            to=[subscriber_email]
        )
    else:
        print('*** Weekly task to send an email to a subscriber ***')
        msg = EmailMultiAlternatives(
            subject=f'Здравствуй, {subscriber_name}. Новые статьи за прошлую неделю в вашем разделе!',
            from_email=DEFAULT_FROM_EMAIL,
            to=[subscriber_email]
        )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    print(f'Name: {subscriber_name}')
    print(f'Email: {subscriber_email}')
    print(f'Content: {html_content}')
    print('*** Task completed ***')


@shared_task
def weekly_send_mail_task():
    print('*** Weekly task ***')
    categories = Category.objects.all()
    for category in categories:
        posts_for_category = []
        week_number_last = datetime.now().isocalendar()[1] - 1
        posts_list = Post.objects.filter(category__id=category.id, time_of_creation__week=week_number_last)
        for post in posts_list:
            posts_for_category.append(post)
        for subscriber in category.subscribers.all():
            subscriber_name = subscriber.username
            subscriber_email = subscriber.email
            html_content = render_to_string(
                'email/weekly_newsletter_mail.html', {
                    'username': subscriber_name,
                    'category': category,
                    'posts': posts_list,
                    'week': week_number_last,
                }
            )
            send_mail_task.delay(subscriber_name, subscriber_email, html_content, weekly_task=True)
    print('*** Weekly task completed ***')
