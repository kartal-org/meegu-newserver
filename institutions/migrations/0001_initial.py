# Generated by Django 4.0.2 on 2022-02-16 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import institutions.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('contact', models.CharField(max_length=20, unique=True)),
                ('address', models.TextField()),
                ('profileImage', models.ImageField(blank=True, null=True, upload_to=institutions.models.upload_to, verbose_name='Institution Profile Image')),
                ('profileCover', models.ImageField(blank=True, null=True, upload_to=institutions.models.upload_to, verbose_name='Institution Profile Cover')),
                ('about', models.TextField(blank=True, max_length=500, verbose_name='about')),
                ('email', models.EmailField(max_length=254)),
                ('isActive', models.BooleanField(default=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
                ('storageUsed', models.IntegerField(default=0)),
                ('storageLimit', models.IntegerField(default=0)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('disapproved', 'Disapproved')], default='pending', max_length=20)),
                ('document', models.FileField(blank=True, null=True, upload_to=institutions.models.upload_verification)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateModified', models.DateTimeField(auto_now=True)),
                ('institution', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='institutions.institution')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.institution')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=institutions.models.upload_to, verbose_name='Department-Logo')),
                ('isActive', models.BooleanField(default=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.institution')),
            ],
        ),
    ]
