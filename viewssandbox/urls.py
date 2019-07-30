from django.urls import path

from . import views

app_name = 'viewssandbox'

urlpatterns = [
    #path('', views.simple, name='simple'),
    #path('test/', views.test, name='test'),
    path('form_test/', views.form_test, name='form_test'),
    #path('fbvlist/', views.fbvlist),
    #path('cbvlist/', views.UserInfoListView.as_view(), name='cbvlist'),
  ]