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
    lookup_field = 'guid'


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


class EntityThreadViewSet(viewsets.ModelViewSet):

    serializer_class = ThreadSerializer

    def get_queryset(self):
        return Thread.objects.filter(entity__guid=self.kwargs['entity_guid'])


class UserOwnedThreadViewSet(viewsets.ModelViewSet):

    serializer_class = ThreadSerializer

    def get_queryset(self):
        return Thread.objects.filter(owner__username=self.kwargs['user_username'])


class UserThreadViewSet(viewsets.ModelViewSet):

    serializer_class = ThreadSerializer

    def get_queryset(self):
        return Thread.objects.filter(participant__username=self.kwargs['user_username'])


class UserMessageViewSet(viewsets.ModelViewSet):

    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(author__username=self.kwargs['user_username'])


class ThreadMessageViewSet(viewsets.ModelViewSet):

    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(thread=self.kwargs['thread_pk']).order_by('creation')
