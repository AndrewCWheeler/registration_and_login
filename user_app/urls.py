from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registering', views.registering),
    path('registered', views.registered),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
]