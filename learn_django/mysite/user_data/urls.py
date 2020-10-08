from django.urls import path

# from django.conf.urls import url

from . import views

app_name = 'user_data'

urlpatterns = [
    path('', views.index, name='index'),
    path('view_user_details', views.view_details.as_view(), name='view'),
    path('input_user_details', views.get_name, name='input'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('all_results', views.all_results.as_view(), name='all_results')
]