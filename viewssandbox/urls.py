from django.urls import path

from . import views

app_name = 'viewssandbox'

urlpatterns = [
    path('landing', views.landing, name='landing'),
    path('simple', views.simple, name='simple'),
    path('test/', views.test, name='test'),
    path('form_test/', views.form_test, name='form_test'),
    path('modelform_test/', views.model_form_test, name='model_form_test'),
    path('fbvlist/', views.fbvlist, name='fbvlist'),
    path('cbvlist/', views.UserInfoListView.as_view(), name='cbvlist'),
    path('reporter/<int:pk>', views.ReporterDetailView.as_view(), name='reporter'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name ='article'),
  ]