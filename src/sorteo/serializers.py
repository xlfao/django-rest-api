import uuid
import json
from rest_framework import serializers
from .models import Raffle, TokenEmail
from django.contrib.auth import get_user_model
from utils.worker import Worker

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
        )

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data, is_active=False)
        token = TokenEmail()
        token.user = user
        token.token = uuid.uuid4()
        token.save()
        Worker.send_task("email.start", args=([user.id]), queue="default")
        return user
    


class RaffleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Raffle
        fields = ('id', 'email', 'created_at')

