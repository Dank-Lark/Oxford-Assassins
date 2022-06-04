from urllib import request
from django.shortcuts import render

# Admin Views:
#   admin_home
#   admin_about
#   admin_cabal
#   admin_users
#   admin_games

def home(request):
    context = {}
    return render(request, 'admin/admin_home.html', context)

def about(request):
    context = {}
    return render(request, 'admin/admin_about.html', context)

def cabal(request):
    context = {}
    return render(request, 'admin/admin_cabal.html', context)

def users(request):
    context = {}
    return render(request, 'admin/admin_users.html', context)
    
def games(request):
    context = {}
    return render(request, 'admin/admin_games.html', context)