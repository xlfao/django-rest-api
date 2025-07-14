# Django REST Framework - API Sorteo

DRF + Celery

_Antes de comenzar a utilizar la API se debe considerar utilizar autenticación básica con los datos:_

Username: fabian
Password: django-rest-api

### Ejemplo:

```
curl --request POST \
  --url http://127.0.0.1:6901/users/ \
  --header 'Authorization: Basic ZmFiaWFuOmRqYW5nby1yZXN0LWFwaQ==' \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "nuevo1",
	"email": "nuevo1@aravena.dev",
	"first_name": "Nuevo",
	"last_name": "Uno"
}'
```


## 1 - INICIAR PROYECTO CON DOCKER
Proyecto optimizado para inicar utilizando Docker y docker-compose.

_Inicialmente el archivo docker-compose.yml está configurado para iniciar la API en http://localhost:6901/_

1. Levantar servicio:

```
docker-compose up -d
```

2. Leer registros de LOG del servicio:

```
docker-compose logs -f
```


## 2 - Endpoints habilitados

### Usuarios

1. Crear nuevo usuario (método POST):
- POST a: /users/
- Header: Authorization: Basic ZmFiaWFuOmRqYW5nby1yZXN0LWFwaQ==
- Payload:
```
{
	"username": "nuevo2",
	"email": "nuevo2@aravena.dev",
	"first_name": "Nuevo",
	"last_name": "Dos"
}
```

### Ejemplo:

```
curl --request POST \
  --url http://127.0.0.1:6901/users/ \
  --header 'Authorization: Basic ZmFiaWFuOmRqYW5nby1yZXN0LWFwaQ==' \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "nuevo2",
	"email": "nuevo2@aravena.dev",
	"first_name": "Nuevo",
	"last_name": "Dos"
}'
```


2. Activar cuenta de correo (método GET):
- GET a: /activar/<token>

### Ejemplo:

```
curl --request GET \
  --url http://127.0.0.1:6901/activar/0d0ed1bf-adfd-46e4-9c66-42e8e166f3fa
```


3. Crear contraseña a usuario de autenticación básica (método PUT):
_Se debe activar antes el usuario (paso 2.) para poder cambiar contraseña_
- PUT a: /createpassword
- Header: Authorization: Basic ZmFiaWFuOmRqYW5nby1yZXN0LWFwaQ==

### Ejemplo:

```
curl --request PUT \
  --url http://127.0.0.1:6901/createpassword \
  --header 'Authorization: Basic bnVldm86bnVldm9udWV2bzI=' \
  --header 'Content-Type: application/json' \
  --data '{
	"password": "nuevaclave"
}'
```


4. Lista de usuarios (método GET):
- GET a: /users
- Header: Authorization: Basic ZmFiaWFuOmRqYW5nby1yZXN0LWFwaQ==

### Ejemplo:

```
curl --request GET \
  --url http://127.0.0.1:6901/users \
  --header 'Authorization: Basic ZmFiaWFuOmRqYW5nby1yZXN0LWFwaQ=='
```



5. Lista de sorteos realizados (método GET):
- GET a: /raffles
- Header: Authorization: Basic ZmFiaWFuOmRqYW5nby1yZXN0LWFwaQ==

### Ejemplo:

```
curl --request GET \
  --url http://127.0.0.1:6901/raffles \
  --header 'Authorization: Basic ZmFiaWFuOmRqYW5nby1yZXN0LWFwaQ=='
```


6. Realizar SORTEO para asignar un ganador (método GET):
- GET a: /newraffle
- Header: Authorization: Basic ZmFiaWFuOmRqYW5nby1yZXN0LWFwaQ==

### Ejemplo:

```
curl --request GET \
  --url http://127.0.0.1:6901/newraffle \
  --header 'Authorization: Basic ZmFiaWFuOmRqYW5nby1yZXN0LWFwaQ=='
```



## 3 - Instalación desde cero

1. Acceder por consola y ejecutar el comando:
    ```
    python manage.py migrate
    ```

    _Utilizando docker-compose podemos usar el comando:_
    ```
    docker-compose exec api python manage.py migrate
    ```

    Con esto crearemos las tablas en la nueva base de datos.

2. Crear usuario inicial por consola, ejecutar el comando:
    ```
    python manage.py createsuperuser --email fabian@aravena.dev --username fabian
    ```
    _Ingresar contraseña: django-rest-api_



## 4 - Estructura de carpetas

Estructura de carpetas estándar de Django.

* /src: contiene todo el código fuente de la aplicación
* * /src/api: directorio que contiene el archivo settings.py y urls.py
* * /src/sorteo: APP de Django con endpoints de la API
* /config: contiene archivo requirements.txt del proyecto



## Creado por

* [Fabián Aravena](mailto://fabian@aravena.dev) - Usando Django + DRF + Celery + Redis + RabbitMQ
