from django.urls import path, include

from rest_framework import routers

from .views import UserViewSet, GroupViewSet, UserDataView

from django.contrib import admin

# from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='usi')
router.register(r'groups', GroupViewSet)
router.register(r'userdata', UserDataView)

app_name = 'restapi'

urlpatterns = [
   path('test/', include(router.urls)),
]