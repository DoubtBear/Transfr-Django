from django.contrib import admin
from .models import Profile




# Register your models here.

admin.site.site_header = 'Transfr Admin Terminal'
admin.site.register(Profile)

