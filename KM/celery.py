from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KM.settings')

app = Celery('KM')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Tehran')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'check-knowledge-evey-day-at-17': {
        'task': 'KnowledgeManagement.tasks.turn_exp_2_knowledge_expert',
        'schedule': crontab(hour=17, minute=10),
    }

}

# Celery Schedules - https://docs.celeryproject.org/en/stable/reference/celery.schedules.html

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')