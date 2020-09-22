from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from mahasiswa import views 

from . import views

urlpatterns = [
    path('', views.index),
    path('<id>/', views.detail),
    path('<id>/delete/', views.delete),
    path('<id>/update/', views.update),
    # path('index/',  views.CrudView.as_view(), name='mahasiswa'),
]
