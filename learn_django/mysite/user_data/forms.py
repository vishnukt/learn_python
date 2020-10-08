from django import forms


class user_details(forms.Form):
    name = forms.CharField(label='Full Name', max_length=100)
    town = forms.CharField(label='Home Town', max_length=100)
    age = forms.IntegerField(label='Age')