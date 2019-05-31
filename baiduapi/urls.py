from django.urls import path
from baiduapi import views


urlpatterns = [
    path('test/', views.test, name='test'),
]