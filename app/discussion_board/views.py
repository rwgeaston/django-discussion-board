# pylint: disable=too-many-ancestors
from rest_framework import viewsets
from rest_framework import filters

from .models import Entity
from .models import Thread
from .models import Message
from .serializers import User
from .serializers import UserSerializer
from .serializers import EntitySerializer
from .serializers import ThreadSerializer
from .serializers import MessageSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class EntityViewSet(viewsets.ModelViewSet):

    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class ThreadViewSet(viewsets.ModelViewSet):

    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('creation',)


class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('creation',)
