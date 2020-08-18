from django.urls import path, re_path
from hello_world import views


urlpatterns = [
	re_path(r'^$', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('better/', views.better, name='better'),
]