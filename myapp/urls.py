from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.helloworld),
    path('url/task', views.home)
]
