from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
]