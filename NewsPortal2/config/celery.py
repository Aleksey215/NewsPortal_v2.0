import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('NewsPortal2')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'weekly_send_mails': {
        'task': 'news.tasks.weekly_send_mail_task',
        'schedule': crontab(hour=8, minute=00, day_of_week='monday'),
    }
}
