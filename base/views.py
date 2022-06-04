from urllib import request
from django.shortcuts import render

# Base Views:
#   home
#   about
#   cabal
#   discord

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)

def cabal(request):
    context = {}
    return render(request, 'base/cabal.html', context)

def discord(request):
    context = {}
    return render(request, 'base/discord.html', context)