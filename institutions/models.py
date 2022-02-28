from django.db import models
from accounts.models import Account
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver


def upload_to(instance, filename):
    return "institutionProfile/{filename}".format(filename=filename)


def upload_verification(instance, filename):
    return "verifications/{filename}".format(filename=filename)


class Institution(models.Model):
    name = models.CharField(max_length=255, unique=True)
    contact = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    profileImage = models.ImageField(_("Institution Profile Image"), upload_to=upload_to, blank=True, null=True)
    profileCover = models.ImageField(_("Institution Profile Cover"), upload_to=upload_to, blank=True, null=True)
    about = models.TextField(_("about"), max_length=500, blank=True)
    email = models.EmailField()
    creator = models.ForeignKey(Account, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    storageUsed = models.IntegerField(default=0)
    storageLimit = models.IntegerField(default=0)

    class ActiveInstitutionManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(isActive=True)

    objects = models.Manager()
    active = ActiveInstitutionManager()

    def __str__(self):
        return self.name


class Verification(models.Model):

    options = (
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("disapproved", "Disapproved"),
    )

    institution = models.OneToOneField(Institution, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=options, default="pending")
    document = models.FileField(upload_to=upload_verification)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.institution.name, self.status)


@receiver(post_save, sender=Verification)
def apply_verification_handler(created, instance, *args, **kwargs):
    """
    Automatically set is_verified property of Institution model if verification is approved.
    """

    if instance.status == "approved":
        institution = Institution.objects.get(id=instance.institution.id)
        institution.is_verified = True
        institution.save()


class Department(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(_("Department-Logo"), upload_to=upload_to, blank=True, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    class ActiveManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(isActive=True)

    objects = models.Manager()
    active = ActiveManager()

    def __str__(self):
        return self.name


class Member(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["user", "institution"]

    class ActiveMembersManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(isActive=True)

    objects = models.Manager()
    active = ActiveMembersManager()

    def __str__(self):
        return "%s %s-%s" % (self.user.first_name, self.user.last_name, self.institution.name)


@receiver(post_save, sender=Institution)
def add_institution_creator_as_a_member_handler(created, instance, *args, **kwargs):

    if created:
        member = Member.objects.create(user=instance.creator, institution=instance, isActive=True)
        member.save()
