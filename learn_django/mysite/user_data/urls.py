from django.urls import path

from . import views

app_name = 'user_data'

urlpatterns = [
    path('', views.index, name='index'),
    path('view_user_details', views.view_details.as_view(), name='view'),
    path('input_user_details', views.get_name, name='input'),
]