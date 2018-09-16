from django.db import models
from django.conf import settings


class Entity(models.Model):
    name = models.CharField(max_length=100)


class Thread(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='owned_threads')
    title = models.CharField(max_length=200)
    entity = models.ForeignKey(Entity, on_delete=models.PROTECT, related_name='threads')
    creation = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='threads')


class Message(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    index = models.IntegerField()

    text = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            'index',
            'thread',
        )
