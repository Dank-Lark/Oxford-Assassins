from urllib import request
from django.shortcuts import render

# Games Views:
#   game_list
#   game

def gameList(request):
    context = {}
    return render(request, 'games/game_list.html', context)

def game(request):
    context = {}
    return render(request, 'games/game.html', context)
