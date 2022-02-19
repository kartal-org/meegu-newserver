# Generated by Django 4.0.2 on 2022-02-14 00:13

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='profileCover',
            field=models.ImageField(blank=True, default='userProfile/coverDefault_pdrisr.jpg', null=True, upload_to=accounts.models.upload_to, verbose_name='ProfileCover'),
        ),
        migrations.AddField(
            model_name='account',
            name='profileImage',
            field=models.ImageField(blank=True, default='userProfile/default_egry2i.jpg', null=True, upload_to=accounts.models.upload_to, verbose_name='ProfileImage'),
        ),
    ]
