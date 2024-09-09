from django.http import HttpResponse
from django.shortcuts import render
from . models import Employ

def index(request):
  employeed = Employ.objects.all()
  return render(request,'employindex.html', {'employeed': employeed})



