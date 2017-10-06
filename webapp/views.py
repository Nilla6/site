from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, 'webapp/home.html')

def about(request):
	return render(request, 'webapp/about.html')

def gallery(request):
	return render(request, 'webapp/gallery.html')
