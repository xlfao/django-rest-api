import importlib
from utils.log import Log
from celery import Celery

log = Log.get(__name__)
name = "worker"

task_packages = ['sorteo']
for task in task_packages:
    importlib.import_module(f"worker.{task}.tasks")

app = Celery('worker')
app.config_from_object('worker.config')
