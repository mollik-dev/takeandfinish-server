from django.shortcuts import render
from django.http import HttpResponse
from .models import Level, LevelRating

# Create your views here.
def view_level(request, id):
	try:
		level = Level.objects.get(pk=id)
	except:
		return HttpResponse('no such level!')
	return HttpResponse(level.level_content)

def main_page(request):
	return render(request, "pages/mainpage.html")

def profile_page(request, id):
	pass

def users_levels_page(request, id):
	pass


def login_page(request):
	return render(request, "pages/loginpage.html")

def register_page(request):
	return HttpResponse('register')