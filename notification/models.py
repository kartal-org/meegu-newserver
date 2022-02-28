from django.db import models
from accounts.models import Account
from institutions.models import Verification
from workspaces.models import File
from django.db.models.signals import post_save
from django.dispatch import receiver


class Notification(models.Model):

    options = (("verification", "verification"), ("submission", "submission"), ("recommendation", "recommendation"))

    message = models.TextField()
    isRead = models.BooleanField(default=False)
    type = models.CharField(max_length=25)
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name="sender+")
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name="receiver+")
    redirectID = models.IntegerField(null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

    class UnreadNofif(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(isRead=False)

    objects = models.Manager()
    unread = UnreadNofif()

    class Meta:
        ordering = ["-dateModified"]

    def __str__(self) -> str:
        return self.message


@receiver(post_save, sender=Verification)
def apply_verification_handler(created, instance, *args, **kwargs):

    print(instance.status)
    if instance.status == "approved":

        notif = Notification.objects.create(
            sender=Account.objects.get(pk=1),
            type="verification",
            message="%s verification application is approved!" % instance.institution.name,
            redirectID=instance.institution.id,
            receiver=instance.institution.creator,
        )

        notif.save()
    if instance.status == "disapproved":

        notif = Notification.objects.create(
            sender=Account.objects.get(pk=1),
            type="verification",
            message="%s verification application is disapproved!" % instance.institution.name,
            redirectID=instance.institution.id,
            receiver=instance.institution.creator,
        )

        notif.save()


@receiver(post_save, sender=File)
def submission_notify_adviser_handler(created, instance, *args, **kwargs):

    if instance.status == "submitted":
        if instance.workspace.adviser:
            notif = Notification.objects.create(
                # sender=Account.objects.get(pk=1),
                type="submission",
                message="There is a new submission in your classroom %s" % instance.workspace.name,
                redirectID=instance.id,
                receiver=instance.workspace.adviser,
            )

            notif.save()
