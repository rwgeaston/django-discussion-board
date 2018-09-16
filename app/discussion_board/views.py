# pylint: disable=too-many-ancestors
from rest_framework import viewsets
from rest_framework import filters

from .models import Thread
from .serializers import ThreadSerializer


class ThreadViewSet(viewsets.ModelViewSet):

    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('creation',)
