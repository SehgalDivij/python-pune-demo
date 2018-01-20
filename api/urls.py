"""jenkins_demo/api URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url('^whoami/', views.identify, name='identify_me'),
]

