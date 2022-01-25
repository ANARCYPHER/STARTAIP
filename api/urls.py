from django.urls import path
from . import views

urlspatterns = [
    path('', views.getData),
    path('add/', views.addItem),
]