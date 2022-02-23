from django.db import models
from accounts.models import Account
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return "pdf/{filename}".format(filename=filename)


# Create your models here.


class Workspace(models.Model):
    class ActiveWorkspacesManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(isActive=True)

    class InActiveWorkspaces(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(isActive=False)

    name = models.CharField(max_length=25)
    creator = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="creator+")
    members = models.ManyToManyField(Account, related_name="members+")
    adviser = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="adviser+", null=True, blank=True)
    isActive = models.BooleanField(default=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    activeWorkspaces = ActiveWorkspacesManager()
    inActiveWorkspaces = ActiveWorkspacesManager()

    def __str__(self):
        return self.name


class File(models.Model):
    FILE_STATUS = [
        ("ongoing", "Ongoing"),
        ("submitted", "Submitted"),
        ("accepted", "Accepted"),
        ("recommended", "Recommended"),
        ("rejected", "Rejected"),
        ("published", "Published"),
    ]

    class ActiveFilesManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(isActive=True)

    name = models.CharField(max_length=60)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to=upload_to, null=True, blank=True)
    richText = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=12, choices=FILE_STATUS, default="ongoing")
    isActive = models.BooleanField(default=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    active = ActiveFilesManager()

    def __str__(self):
        return self.name
