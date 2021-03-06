# Generated by Django 4.0.2 on 2022-02-12 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0002_workspace_adviser_workspace_creator_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateModified', models.DateTimeField(auto_now=True)),
                ('customFor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workspaces.workspace')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateModified', models.DateTimeField(auto_now=True)),
                ('tags', models.ManyToManyField(to='workspaces.Tag')),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspaces.workspace')),
            ],
        ),
    ]
