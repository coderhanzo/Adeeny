from django.contrib import admin
from .models import Mosque, Sermon, Annoucement

# Register your models here.
admin.site.register(Mosque)
admin.site.register(Sermon)
admin.site.register(Annoucement)