from urllib import request
from django.shortcuts import render

# Base Views:
#   home
#   about
#   blog
#   blog_post
#   cabal
#   discord

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)

def blog(request):
    context = {}
    return render(request, 'base/blog.html', context)

def blogPost(request):
    context = {}
    return render(request, 'base/blog_post.html', context)

def cabal(request):
    context = {}
    return render(request, 'base/cabal.html', context)

def discord(request):
    context = {}
    return render(request, 'base/discord.html', context)