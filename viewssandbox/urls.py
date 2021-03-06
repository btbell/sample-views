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
  path('fbv_filtered_sort_list/', views.fbv_filtered_sort_list, name='fbv_filtered_sort_list'),
  path('cbvlist/', views.UserInfoListView.as_view(), name='cbvlist'),
  path('cbv_sortable_list/', views.UserInfoSortableListView.as_view(), name='cbv_sortable_list'),
  path('cbv_custom_sortable_list/', views.UserInfoCustomSortableListView.as_view(), name='cbv_custom_sortable_list'),
  path('cbv_filtered_sortable_list/', views.UserInfoFilteredSortableListView.as_view(), name='cbv_filtered_sortable_list'),
  path('search/', views.UserSearchListView.as_view(), name='cbvsearch'),
  path('reporters/', views.ReporterListView.as_view(), name='reporters'),
  path('reporters/detail/<int:pk>', views.ReporterDetailView.as_view(), name='reporters-detail'),
  path('articles/', views.ArticleListView.as_view(), name='articles'),
  path('articles/<int:pk>', views.ArticleDetailView.as_view(), name ='article-detail'),
  path('tutorial/<int:pk>', views.TutorialDetailView.as_view(), name='tutorial-detail'),
  path('tutorials/', views.TutorialListView.as_view(), name='tutorials'),
]