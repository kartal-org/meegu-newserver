# Generated by Django 4.0.2 on 2022-02-16 06:25

from django.db import migrations, models
import institutions.models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='document',
            field=models.FileField(default=1, upload_to=institutions.models.upload_verification),
            preserve_default=False,
        ),
    ]
