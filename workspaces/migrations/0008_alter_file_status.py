# Generated by Django 4.0.2 on 2022-02-16 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0007_file_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='status',
            field=models.CharField(choices=[('ongoing', 'Ongoing'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('published', 'Published')], default='ongoing', max_length=12),
        ),
    ]
