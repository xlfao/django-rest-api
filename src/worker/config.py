import os
from kombu import Exchange, Queue

BROKER_URL = os.getenv('CELERY_BROKER_URL',
                       'pyamqp://django-rest-api:djangorestapi@rabbitmq:5672/api')
BROKER_TRANSPORT_OPTIONS = {'fanout_prefix': True}
BROKER_TRANSPORT_OPTIONS = {'fanout_patterns': True}
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 60 * 60 * 1}

CELERY_RESULT_BACKEND = os.getenv(
    'CELERY_RESULT_BACKEND', 'redis://redis:6379/0')
CELERY_TIMEZONE = 'America/Santiago'
CELERY_ENABLE_UTC = True
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 1  # En segundos
CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_QUEUES = (
    Queue('default', Exchange('default', type='direct'),
          routing_key='default'),
    )
DJANGO_SETTINGS_MODULE = 'api.settings'