# Generated by Django 3.2.8 on 2022-02-27 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriptionplan',
            options={'ordering': ('price',)},
        ),
    ]