from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class user_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    home_town = models.CharField(max_length=200)
    age = models.IntegerField

    def __str__(self):
        return self.full_name