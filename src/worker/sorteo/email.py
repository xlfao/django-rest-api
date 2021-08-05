import smtplib 
from datetime import datetime
from sorteo.models import TokenEmail
from utils.log import Log
from django.contrib.auth import get_user_model
from api.settings import SITE_URL_API
from email import message


class Email(object):
    """ Email básico en Python """
    
    log = Log.get(__name__)

    def start(self, user_data):
        start = datetime.now()
        response = {"status": False, "user_data": user_data}
        user = get_user_model().objects.filter(pk=user_data).first()
        token = TokenEmail.objects.filter(user=user).first()
        
        url_active = f"{SITE_URL_API}/activar/{token.token}"
        msg = message.Message()
        msg['Subject'] = 'Validar cuenta de correo'
        msg['From'] = 'djangorestapi.cuenta@gmail.com'
        msg['To'] = user.email
        msg.add_header('Content-Type','text/html')
        msg.set_payload(f"""Hola {user.first_name} {user.last_name}!<br/> <br/> 
        <b>Email</b> enviando desde <b>Python</b> <br/><br/> 
        Clic en enlace para activar cuenta: <br/><br/> 
        Nombre de usuario: <b>{user.username}</b> <br/><br/> 
        <a href="{url_active}">{url_active}</a> <br/><br/> 
        """.encode('UTF-8'))
        
        try: 
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            smtp.login(msg['From'], "django-rest-api")
            smtp.sendmail(msg['From'], [msg['To']], str(msg.as_string()).encode('UTF-8'))
            smtp.quit()
            response.update({'status': True, 'message': 'Correo enviado.'})
        except Exception as e: 
            self.log.error({"Error": "Compruebe credenciales del servicio de correo.", "exception": str(e)})
            self.log.info({"email_from": msg['From'], "email_to": msg['To'], "token": token.token if token else None})

        response.update({"time": (datetime.now() - start).total_seconds()})
        return response