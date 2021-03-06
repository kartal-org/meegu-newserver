# Generated by Django 4.0.2 on 2022-02-26 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0008_alter_file_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='status',
            field=models.CharField(choices=[('ongoing', 'Ongoing'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('recommended', 'Recommended'), ('rejected', 'Rejected'), ('published', 'Published')], default='ongoing', max_length=12),
        ),
    ]
