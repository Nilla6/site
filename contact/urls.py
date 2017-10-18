from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from contact.models import ContactMe
from . import views

urlpatterns = [
	url(r'^', views.contact, name ='Contact'),
	]
