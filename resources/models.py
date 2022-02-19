from django.db import models
from institutions.models import Institution
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return "pdf/{filename}".format(filename=filename)

# Create your models here.


class Resource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    isExclusive = models.BooleanField(default=False)
    isActive = models.BooleanField(default=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    imports = models.IntegerField(default=0)
    richText = models.TextField(blank=True, null=True)
    pdf = models.FileField(upload_to=upload_to, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.full_clean()

        super().save(*args, **kwargs)

    class ActiveResourcesManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(isActive=True)

    objects = models.Manager()
    active = ActiveResourcesManager()

    class Meta:
        ordering = ("-dateUpdated",)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Resource)
def add_resource_size(created, instance, *args, **kwargs):

    # breakpoint()
    if created:
        if instance.pdf != None:
            institution = Institution.objects.get(pk=instance.institution.id)
            institution.storageUsed = institution.storageUsed + instance.pdf.size
            institution.save()
