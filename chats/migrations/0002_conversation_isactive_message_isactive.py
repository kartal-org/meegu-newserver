# Generated by Django 4.0.2 on 2022-02-16 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='message',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
