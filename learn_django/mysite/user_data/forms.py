from django import forms

from .models import user_data

from django.forms import ModelForm


class user_details(ModelForm):
    class Meta:
        model = user_data
        fields = ('user', 'full_name', 'home_town', 'age')