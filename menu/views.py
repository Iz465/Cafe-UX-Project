from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu

def index(request):
  return render(request, 'menu-index.html')

def listMenuPage(request) :
  data = Menu.objects.all()
  context = {"Menu": data}
  return render(request, "menu/templates/menu-index.html", context)