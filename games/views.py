from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from games.models import Game, Flag, GameScript, EventScript, ConfigScript

####################################################################################################

@login_required(login_url='login')
def play(request, id=-1):
    '''User side view of '''
    if id == -1:
        # Overview Screen
        print("Gotcha!")
        return redirect('home')

    # Specific ID Screen
    print("Gotcha!")
    return redirect('home')

####################################################################################################

@login_required(login_url='login')
def manage(request):
    '''Management overview, links to Games, Flags, GameScripts, EventScripts, and ConfigScripts'''
    if not request.user.is_staff:
        return redirect('play')
    
    context = { 
        'count_games': Game.objects.count(), 
        'count_flags': Flag.objects.count(), 
        'count_scripts': GameScript.objects.count(), 
        'count_events': EventScript.objects.count(), 
        'count_configs': ConfigScript.objects.count(), 
    }
    return render(request, 'games/manage.html', context)

####################################################################################################

@login_required(login_url='login')
def manageFlags(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')

    if id == -1:
        context = { 'flags': Flag.objects.all() }
        return render(request, 'games/manage_flags.html', context)

    # Specific ID Screen
    pass

####################################################################################################

@login_required(login_url='login')
def newFlag(request):
    if not request.user.is_staff:
        return redirect('play')

    context = { 
        'object_type': "Flag",
        'form': None
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def manageGames(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')

    if id == -1:
        context = { 'games': Game.objects.all() }
        return render(request, 'games/manage_games.html', context)

    # Specific ID Screen
    pass

####################################################################################################

@login_required(login_url='login')
def newGame(request):
    if not request.user.is_staff:
        return redirect('play')

    context = { 
        'object_type': "Game",
        'form': None
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def manageGameScripts(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')
    
    if id == -1:
        context = { 'scripts': GameScript.objects.all() }
        return render(request, 'games/manage_gamescripts.html', context)

    # Specific ID Screen
    pass

####################################################################################################

@login_required(login_url='login')
def newGameScript(request):
    if not request.user.is_staff:
        return redirect('play')

    context = { 
        'object_type': "Script",
        'form': None
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def manageEventScripts(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')
    
    if id == -1:
        context = { 'events': EventScript.objects.all() }
        return render(request, 'games/manage_eventscripts.html', context)

    # Specific ID Screen
    pass

####################################################################################################

@login_required(login_url='login')
def newEventScript(request):
    if not request.user.is_staff:
        return redirect('play')

    context = { 
        'object_type': "Event",
        'form': None
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def manageConfigScripts(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')
    
    if id == -1:
        context = { 'configs': ConfigScript.objects.all() }
        return render(request, 'games/manage_configscripts.html', context)

    # Specific ID Screen
    pass

####################################################################################################

@login_required(login_url='login')
def newConfigScript(request):
    if not request.user.is_staff:
        return redirect('play')

    context = { 
        'object_type': "Config",
        'form': None
    }
    return render(request, 'games/edit.html', context)
