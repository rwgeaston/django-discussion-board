from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Entity(models.Model):
    # Entities are stored in another system; other details are there.
    guid = models.CharField(max_length=36, unique=True)

    def __str__(self):
        return self.guid


class Thread(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='owned_threads')
    title = models.CharField(max_length=200)
    entity = models.ForeignKey(Entity, on_delete=models.PROTECT, related_name='threads', null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(User, related_name='threads')

    def __str__(self):
        return f"{self.pk}) {self.title}"


class Message(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    creation = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    text = models.TextField()
