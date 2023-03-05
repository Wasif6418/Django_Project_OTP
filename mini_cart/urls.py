"""mini_cart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('accounts.urls')),
    path('home', include('cart.urls')),
    path('admin/', admin.site.urls),
]