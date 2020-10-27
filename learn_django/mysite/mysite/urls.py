"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import include, path

from rest_framework import routers

from restapi import views

from rest_framework.authtoken import views as tokenapiview

# from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'userdata', views.UserDataView)

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('user_data/', include('user_data.urls')),
    path('admin/', admin.site.urls),
    path('polls/accounts/', include('django.contrib.auth.urls')),
    # url(r"^polls/accounts/", include("django.contrib.auth.urls")),
    # url(r'^restapi/', include(restapi.urls, namespace="restapi")),
    # path('restapi/', include('restapi.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('restapi/test/', include(router.urls)),
    path('restapi/test/login_token', tokenapiview.obtain_auth_token),
    path('restapi/test/apiview/', views.UserDataApiView.as_view()),
    path('restapi/test/apiview/<int:pk>/', views.UserDataPutApiView.as_view()),
]
