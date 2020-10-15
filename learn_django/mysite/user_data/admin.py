from django.contrib import admin

from django.contrib.auth.models import User

from .models import user_data

admin.site.register(user_data)
