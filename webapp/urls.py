from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name ='Home'),
	url(r'^about/', views.about, name = 'About'),
	url(r'^gallery/', views.gallery, name = 'Gallery'),
	]
