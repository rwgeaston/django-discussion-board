from django.apps import apps
from rest_framework import serializers

from .models import Entity
from .models import User
from .models import Thread
from .models import Message


User = apps.get_model(User)


class UserSerializer(serializers.ModelSerializer):
    threads = serializers.StringRelatedField(
        many=True,
        read_only=True,
    )
    owned_threads = serializers.StringRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = User
        fields = (
            'username',
            'threads',
            'owned_threads',
        )


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'


class ThreadSerializer(serializers.ModelSerializer):
    entity = serializers.SlugRelatedField(queryset=Entity.objects.all(), slug_field='guid')
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    participants = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', many=True)

    class Meta:
        model = Thread
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Message
        fields = '__all__'
