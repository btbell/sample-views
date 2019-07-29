from django.urls import path

from . import views

app_name = 'viewssandbox'

urlpatterns = [
    path('', views.simple, name='simple'),
    path('fbvlist/', views.fbvlist),
    path('cbvlist/', views.UserInfoListView.as_view(), name='cbvlist'),
  ]