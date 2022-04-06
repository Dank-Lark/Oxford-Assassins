from urllib import request
from django.shortcuts import render

# Account Views:
#   account
#   login
#   logout
#   register
#   profile

def account(request):
    context = {}
    return render(request, 'account/account.html', context)

def login(request):
    context = {}
    return render(request, 'account/login.html', context)

def logout(request):
    context = {}
    return render(request, 'account/logout.html', context)

def register(request):
    context = {}
    return render(request, 'account/register.html', context)

def profile(request):
    context = {}
    return render(request, 'account/profile.html', context)
