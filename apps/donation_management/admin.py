from django.contrib import admin
from .models import ProjectDonations, Donations

# Register your models here.
admin.site.register(Donations)
admin.site.register(ProjectDonations)