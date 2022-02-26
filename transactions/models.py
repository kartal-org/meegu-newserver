from django.db import models
from django.utils.translation import gettext_lazy as _
from institutions.models import Institution
from institutions.models import Institution
from django.db.models.signals import post_save
from django.dispatch import receiver


def upload_to(instance, filename):
    return "subscriptions/{filename}".format(filename=filename)


# Create your models here.


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(_("PlanImage"), upload_to=upload_to, blank=True, null=True)
    isActive = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    storageLimit = models.PositiveIntegerField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    class ActivePlansManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(isActive=True)

    objects = models.Manager()
    active = ActivePlansManager()

    class Meta:
        ordering = ("price",)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-dateCreated",)

    def __str__(self):
        return "%s - %s" % (self.institution.name, self.dateCreated)


@receiver(post_save, sender=Transaction)
def add_storage_size(created, instance, *args, **kwargs):

    # breakpoint()
    if created:
        institution = Institution.objects.get(pk=instance.institution.id)
        institution.storageLimit = institution.storageLimit + instance.plan.storageLimit
        institution.save()
