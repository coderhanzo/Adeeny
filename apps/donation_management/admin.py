from django.contrib import admin
from .models import ProjectDonation, Donation

# Register your models here.
admin.site.register(Donation)
admin.site.register(ProjectDonation)