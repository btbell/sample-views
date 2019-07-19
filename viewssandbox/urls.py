from django.urls import path

from . import views

app_name = 'viewssandbox'

urlpatterns = [
  path('', views.simple, name='simple'),
  ]