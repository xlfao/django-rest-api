import redis
from worker.config import CELERY_RESULT_BACKEND
from datetime import timedelta
from utils.log import Log

        
class Redis(object):
    """ Clase para funciones de Redis """
    __author__ = "Fabián Aravena Ordóñez"
    __email__ = "fabian@aravena.dev"
    db = redis.from_url(CELERY_RESULT_BACKEND)
    log = Log.get(__name__)
    celery_task = 'celery-task-meta-'
    
    def get_task(self, task_id):
        task_name = f'{self.celery_task}{task_id}'
        response = False
        if self.exists(task_name):
            response = self.db.get(task_name)
        return response
    
    def get_key(self, key):
        response = False
        if self.exists(key):
            response = self.db.get(key)
        return response
    
    def set_key(self, key, value, expiration=None):
        try:
            if expiration:
                response = self.db.setex(key, time=timedelta(
                minutes=expiration), value=value)
            else:
                response = self.db.set(key, value=str(value))
        except Exception as e:
            self.log.error(
                f"REDIS: No se pudo almacenar llave [{key}]. Ocurrio un problema: {e}")
            response = False
        return response
        
    def exists(self, key):
        """ Validar si existe KEY de Redis
            Payload: key
            Response: number
            """
        return self.db.exists(str(key))
    
    def delete(self, key):
        """ Eliminar KEY de Redis
            Payload: key
            """
        return self.db.delete(str(key))
