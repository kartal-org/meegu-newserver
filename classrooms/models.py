from django.db import models
from accounts.models import Account
from workspaces.models import File, Workspace
from institutions.models import Institution
from django.db.models.signals import post_save
from django.dispatch import receiver
from notification.models import Notification

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


@receiver(post_save, sender=Recommendation)
def apply_Recommendation_handler(created, instance, *args, **kwargs):

    if created:
        file = File.objects.get(pk=instance.file.id)
        file.status = "accepted"
        file.save()
        pass


@receiver(post_save, sender=Recommendation)
def apply_NotifyStudent_handler(created, instance, *args, **kwargs):

    if created:
        # what do we need: notify every student:
        # what do we have: file ID
        members = Workspace.objects.get(pk=instance.file.workspace.id).members
        membersID = []

        for x in members.all():
            membersID.append(x.id)
            notif = Notification.objects.create(
                sender=Account.objects.get(pk=1),
                type="accepted",
                message="Your file, %s is accepted and has been recommended by your adviser!" % instance.file.name,
                redirectID=instance.file.id,
                receiver=x,
            )

            notif.save()
            print(x.id)
        #
        # breakpoint()
        pass


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
