
# Generated by Django 3.2.12 on 2022-02-28 05:15

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
