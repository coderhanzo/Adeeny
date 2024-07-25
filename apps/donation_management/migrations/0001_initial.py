# Generated by Django 5.0.6 on 2024-07-25 12:04

import apps.donation_management.models
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Account Name')),
                ('phone_numnber', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Phone Number')),
                ('ammount', models.PositiveIntegerField(blank=True, null=True, verbose_name='Amount')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='WAQF Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('upload_image', models.FileField(blank=True, null=True, upload_to=apps.donation_management.models.ProjectDonation.user_directory_path, verbose_name='Upload Image')),
                ('imams_name', models.CharField(blank=True, max_length=250, null=True, verbose_name="Imam's Name")),
                ('payment_type', models.CharField(blank=True, max_length=250, null=True, verbose_name='Payment Type')),
                ('target_amount', models.PositiveIntegerField(blank=True, null=True, verbose_name='Target Amount')),
            ],
        ),
    ]
