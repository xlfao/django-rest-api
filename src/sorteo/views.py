import uuid
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework import permissions
from sorteo.serializers import RaffleSerializer, UserSerializer
from .models import Raffle, TokenEmail
from random import randrange



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    


class RaffleViewSet(viewsets.ModelViewSet):
    queryset = Raffle.objects.all()
    serializer_class = RaffleSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def activate(request, token, format=None):
    try:
        if request.method == 'GET':
            token = TokenEmail.objects.filter(token=token).first()
            user = token.user
            user.is_active = True
            user.save()
            token.delete()
            return Response({"status": True, "message": "Cuenta activada correctamente."})
    except Exception as e:
        return Response({"status": False, "message": "Token no existe o no es válido."}, 401)


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def password_create(request):
    try:
        user = request.user
    except Exception as e:
        user = False
        return Response(status=404)
    if request.method == 'PUT':
        if user and user.is_active:
            user.set_password(request.data['password'])
            user.save()
            return Response({"status": True, "message": "Contraseña creada correctamente."}, 200)
        else:
            return Response({"status": False, "message": "Usuario inválido o no activado, debe validar su cuenta de correo."}, 401)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def new_raffle(request):
    try:
        if request.method == 'GET':
            raffle = Raffle()
            list_users = User.objects.filter(is_active=True).all()
            number = randrange(list_users.count())
            winner = list_users[number]
            raffle.email = winner.email
            raffle.save()
            return Response({"status": True, "message": "Sorteo generado correctamente. Tenemos un ganador.", 
                            "user_email": winner.email, "user_id": winner.id, "user_name": f"{winner.first_name} {winner.last_name}".strip(), "random_number": number})
    except Exception as e:
        return Response({"status": False, "message": "Ocurrio un problema intentando generar sorteo.", "error": str(e)}, 401)