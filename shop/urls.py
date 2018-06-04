from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.all_list, name='all_list'),
    re_path('^item/(?P<pk>[0-9]+)/$', views.adding_some_popularity, name='popularity')
]