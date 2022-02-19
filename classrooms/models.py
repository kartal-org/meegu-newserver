from django.db import models
from accounts.models import Account
from workspaces.models import File
from institutions.models import Institution

# Create your models here.


class Recommendation(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    adviser = models.ForeignKey(Account, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
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
        return self.title


class Comment(models.Model):
    content = models.TextField()
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
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
        return self.content


class Reply(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    reply_to = models.ForeignKey(Comment, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    class ActiveManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(isActive=True)

    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        ordering = ("-dateUpdated",)
