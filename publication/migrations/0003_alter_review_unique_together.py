# Generated by Django 3.2.8 on 2022-02-27 16:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publication', '0002_article_pdf'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('article', 'user')},
        ),
    ]
