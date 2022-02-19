from django.db import models
from classrooms.models import Recommendation
from institutions.models import Institution, Department
from accounts.models import Account
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Article(models.Model):
    options = [
        ("published", "Published"),
        ("draft", "Draft"),
        ("archive", "Archive"),
    ]

    title = models.CharField(max_length=255, unique=True)
    abstract = models.TextField()
    status = models.CharField(max_length=20)
    recommendation = models.ForeignKey(Recommendation, on_delete=models.SET_NULL, null=True, blank=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    citation = models.TextField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-dateUpdated",)

    @property
    def rating(self):
        return Review.objects.filter(article=self.id).aggregate(Avg("rate"))["rate__avg"]

    def __str__(self):
        return self.title


class Review(models.Model):
    option = [
        (1, "Very Bad"),
        (2, "Bad"),
        (3, "Decent"),
        (4, "Very Good"),
        (5, "Excellent"),
    ]
    comment = models.TextField()
    rate = models.IntegerField()
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-dateUpdated",)

    def __str__(self):
        return "%s-%s %s" % (self.article.title, self.user.first_name, self.user.last_name)


@receiver(post_save, sender=Article)
def add_article_size(created, instance, *args, **kwargs):

    fileSize = instance.recommendation.file.pdf.size
    print(fileSize)
    institution = Institution.objects.get(pk=instance.id)
    institution.storageUsed = institution.storageUsed + fileSize
    institution.save()
