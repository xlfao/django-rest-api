import worker

class Worker(object):
    """ Clase para tareas de Celery """
    __author__ = "Fabián Aravena Ordóñez"
    __email__ = "fabian@aravena.dev"
    
    def send_task(task, args, queue='default'):
        return worker.app.send_task(task, args=args, queue=queue)



