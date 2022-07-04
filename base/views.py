from urllib import request
from django.shortcuts import render

# Base Views:
#   base

def home(request):
    context = {}
    return render(request, 'base/base.html', context)