from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UserModel(serializers.Serializer):
    full_name = serializers.CharField(max_length=200)
    home_town = serializers.CharField(max_length=200)
    age = serializers.IntegerField()
    # class Meta:
    #     model = User
    #     fields = ['url', 'name']
