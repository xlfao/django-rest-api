import logging
from api.settings import DEBUG


class Log(object):
    """ Logs centralizado """
    __author__ = "Fabián Aravena Ordóñez"
    __email__ = "fabian@aravena.dev"

    def get(name, level='DEBUG' if DEBUG else 'INFO'):
        logger = logging.getLogger(name)
        logger.setLevel(level)
        
        ch = logging.StreamHandler()
        ch.setLevel(level)
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s - '
                                      '%(name)s: %(message)s',
                                      datefmt='%Y-%m-%dT%H:%M:%S%Z')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        return logger
