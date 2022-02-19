from django.db import models
from accounts.models import Account

# Create your models here.


class Conversation(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(Account, related_name="chat_members")
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    class ActiveManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(isActive=True)

    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        ordering = ("-dateUpdated",)

    def __str__(self):
        return self.name


class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="sender+")
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="receiver+")
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    class ActiveManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(isActive=True)

    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        ordering = ("-dateUpdated",)

    def __str__(self):
        return self.conversation.name
