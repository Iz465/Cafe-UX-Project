from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu
import sys

def index(request):
  menu = Menu.objects.all()
  return render(request, 'menu-index.html', {'menu': menu})



def run():
  print("Runnnig")
  arg = ""
  if len(sys.argv) < 1:
    return 0
  elif sys.argv[1] == "listMenuPage":
    print("RAN")
    arg = sys.argv[1]
    return Menu.objects.all()

run()

