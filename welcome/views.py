
from django.shortcuts import render
from .models import Welcome

def index(request):
  welcome = Welcome.objects.all()
  return render(request, 'welcome-index.html', {'welcomes': welcome})







