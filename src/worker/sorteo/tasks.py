
from celery import shared_task
from utils.log import Log
from .email import Email

log = Log.get(__name__)
config = {'timeout': 60 * 15}

@shared_task(time_limit=config.get('timeout'), name="email.start")
def start(user_data):
    return Email().start(user_data)