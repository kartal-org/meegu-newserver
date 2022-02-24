from django.db import models
from accounts.models import Account
from publication.models import Article


class LibraryItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["user", "article"]

    def __str__(self):
        return self.article.title
