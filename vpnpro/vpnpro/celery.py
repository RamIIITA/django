
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vpnpro.settings')

app = Celery('vpnpro')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.

app.config_from_object('django.conf:settings') #, namespace='CELERY')

# Load task modules from all registered Django app configs.
app.conf.update(
    CELERY_RESULT_BACKEND='djcelery.backends.cache:CacheBackend',
)

app.autodiscover_tasks(settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

"""
Run the below command on seperate terminal 

=============================================================
celery -A <project name> worker --loglevel=info --beat
=============================================================

above command contains both beat and worker

if you want both of them in seperated terminals then in two seperte terminals run tge below
command

==============================================================
terminal one: celery -A <project name> worker --loglevel=info

terminal two: celery -A <project name> beat --loglevel=info
===============================================================
