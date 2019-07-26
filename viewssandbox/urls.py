from django.urls import path

from . import views

app_name = 'viewssandbox'

urlpatterns = [
    path('', views.simple, name='simple'),
    path('simpletemplate', views.simpletemplate)
    #path('listvw', views.ListView.as_view, name="listvw")
  ]