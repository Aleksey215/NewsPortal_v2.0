from celery import shared_task
from django.core.mail import EmailMultiAlternatives

from config.settings import DEFAULT_FROM_EMAIL

@shared_task
def send_mail_subscribers_task(subscriber_name, subscriber_email, html_content):
    print('*** Launching a task to send an email to a subscriber ***')
    print(f'Name: {subscriber_name}')
    print(f'Email: {subscriber_email}')
    print(f'Content: {html_content}')
    msg = EmailMultiAlternatives(
        subject=f'Здравствуй, {subscriber_name}. Новая статья в вашем разделе!',
        from_email=DEFAULT_FROM_EMAIL,
        to=[subscriber_email]
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    print('*** Task completed ***')
