from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu



def index(request):
  menu = Menu.objects.all()
  return render(request, 'menu-index.html', {'menu': menu})








