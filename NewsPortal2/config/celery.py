import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS-MODULE', 'config.settings')

app = Celery('NewsPortal2')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
