# Generated by Django 5.0.6 on 2024-07-18 10:31

import apps.mosque_management.models
import django.contrib.gis.db.models.fields
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annoucement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='n/a', max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('image', models.FileField(blank=True, null=True, upload_to='user_directory_path')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='File Name')),
                ('file', models.FileField(blank=True, null=True, upload_to=apps.mosque_management.models.MediaFile.user_directory_path)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MediaImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to=apps.mosque_management.models.MediaImage.user_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Mosque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Mosque Name')),
                ('tel', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Phone Number')),
                ('mail', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Address')),
                ('imam', models.CharField(max_length=250, verbose_name="Imam's Name")),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('image', models.FileField(blank=True, null=True, upload_to=apps.mosque_management.models.Mosque.user_directory_path)),
                ('certificate', models.FileField(blank=True, null=True, upload_to=apps.mosque_management.models.Mosque.user_directory_path)),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='Content')),
            ],
        ),
        migrations.CreateModel(
            name='PrayerTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='n/a', max_length=250)),
                ('time', models.TimeField(default='n/a', max_length=250)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='n/a', max_length=250)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('speaker_name', models.CharField(default='n/a', max_length=250)),
                ('sermon_type', models.CharField(choices=[('AUDIO', 'Audio'), ('VIDEO', 'video'), ('DOCUMENT', 'Document')], default='n/a', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('audio', models.ManyToManyField(blank=True, related_name='sermon_audio', to='mosque_management.mediafile')),
                ('docs', models.ManyToManyField(blank=True, related_name='sermon_docs', to='mosque_management.mediafile')),
                ('video', models.ManyToManyField(blank=True, related_name='sermon_video', to='mosque_management.mediafile')),
            ],
        ),
    ]
