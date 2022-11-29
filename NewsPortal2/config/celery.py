import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('NewsPortal2')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
        # Executes every Monday morning at 7:30 a.m.
        'add-every-monday-morning': {
            'task': 'tasks.weekly_send_mail_task',
            'schedule': crontab(hour=19, minute=45, day_of_week=2),
            # 'args': (weekly_emails_to_subscribers),
        },
    }

app.autodiscover_tasks()



