from django.http import HttpResponse
from django.shortcuts import render
from .models import Rewards


def index(request):
  rewards = Rewards.objects.all()
  return render(request, 'index.html', {'rewards': rewards})


def newRewards(request):
  return render(request, 'claimReward.html')