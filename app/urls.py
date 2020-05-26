from . import views
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('feed/', views.feed, name='feed'),
    path('upload/', views.upload, name='upload'),
    path('messages/', views.messages, name='messages'),
    path('statistics/', views.statistics, name='statistics'),
]