# Generated by Django 5.0.6 on 2024-08-07 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosque_management', '0002_alter_mosque_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='n/a', max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('time', models.TimeField(auto_now_add=True, null=True)),
                ('location', models.CharField(blank=True, max_length=250, null=True, verbose_name='Mosque Location')),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('long', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('image', models.FileField(blank=True, null=True, upload_to='user_directory_path')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Annoucement',
        ),
    ]
