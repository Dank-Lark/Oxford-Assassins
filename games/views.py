from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from games.models import Game, Flag, GameScript, EventScript, ConfigScript, XASGroup
from games.forms import *
from django.contrib import messages

def alertErrors(request, form_errors):
    errors = str(
        " ".join(
            map(
                lambda s: s[4:], 
                filter(
                    lambda s: s.startswith("  * "), 
                    form_errors.as_text().split("\n")
                )
            )
        )
    )
    messages.error(request, errors)

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
    '''Management overview, links to Groups, Games, Flags, GameScripts, EventScripts, and ConfigScripts'''
    if not request.user.is_staff:
        return redirect('play')
    
    context = { 
        'count_groups':    XASGroup.objects.count(), 
        'count_games':     Game.objects.count(),
        'count_flags':     Flag.objects.count(), 
        'count_infolore':  InfoLore.objects.count(), 
        'count_scripts':   GameScript.objects.count(), 
        'count_events':    EventScript.objects.count(), 
        'count_configs':   ConfigScript.objects.count(), 
    }
    return render(request, 'games/manage.html', context)

####################################################################################################
####################################################################################################

@login_required(login_url='login')
def manageXASGroups(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')

    if id == -1:
        context = { 'groups': XASGroup.objects.all() }
        return render(request, 'games/manage_groups.html', context)

    xas_group = XASGroup.objects.get(id=id)
    if xas_group is None:
        return redirect('manage_groups')

    if request.method == "POST":
        form = XASGroupForm(request.POST, instance=xas_group)

        if form.is_valid():
            form.save()
            return redirect('manage_groups')
        else:
            alertErrors(request, form.errors)
    else:
        form = XASGroupForm(instance=xas_group)

    context = { 
        'object_type': "Group",
        'new_object': False,
        'form': form,
        'delete_url': "delete_group",
        'object_id': id
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def newXASGroup(request):
    if not request.user.is_staff:
        return redirect('play')

    if request.method == "POST":
        form = XASGroupForm(request.POST)

        if form.is_valid():
            xas_group = form.save(commit=False)
            xas_group.umpire = request.user.assassin
            xas_group.save()
            return redirect('manage_groups')
        else:
            alertErrors(request, form.errors)
    else:
        form = XASGroupForm()

    context = { 
        'object_type': "Group",
        'new_object': True,
        'form': form
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def deleteXASGroup(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')

    if id == -1:
        return redirect('manage_groups')

    xas_group = XASGroup.objects.get(id=id)
    if xas_group is None:
        return redirect('manage_groups')

    if xas_group.umpire != request.user.assassin:
        return redirect('manage_groups')

    xas_group.delete()
    return redirect('manage_groups')

####################################################################################################
####################################################################################################

@login_required(login_url='login')
def manageInfoLore(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')

    if id == -1:
        context = { 'infolores': InfoLore.objects.all() }
        return render(request, 'games/manage_infolore.html', context)

    infolore = InfoLore.objects.get(id=id)
    if infolore is None:
        return redirect('manage_infolore')

    if request.method == "POST":
        form = InfoLoreForm(request.POST, instance=infolore)

        if form.is_valid():
            form.save()
            return redirect('manage_infolore')
        else:
            alertErrors(request, form.errors)
    else:
        form = InfoLoreForm(instance=infolore)

    context = { 
        'object_type': "InfoLore",
        'new_object': False,
        'form': form,
        'delete_url': "delete_infolore",
        'object_id': id
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def newInfoLore(request):
    if not request.user.is_staff:
        return redirect('play')

    if request.method == "POST":
        form = InfoLoreForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('manage_infolore')
        else:
            alertErrors(request, form.errors)
    else:
        form = InfoLoreForm()

    context = { 
        'object_type': "InfoLore",
        'new_object': True,
        'form': form
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def deleteInfoLore(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')

    if id == -1:
        return redirect('manage_infolore')

    infolore = InfoLore.objects.get(id=id)
    if infolore is None:
        return redirect('manage_infolore')

    if infolore.xas_group.umpire != request.user.assassin:
        return redirect('manage_infolore')

    infolore.delete()
    return redirect('manage_infolore')

####################################################################################################
####################################################################################################

@login_required(login_url='login')
def manageConfigScripts(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')
    
    if id == -1:
        context = { 'configs': ConfigScript.objects.all() }
        return render(request, 'games/manage_configscripts.html', context)
    
    config_script = ConfigScript.objects.get(id=id)
    if config_script is None:
        return redirect('manage_configs')

    if request.method == "POST":
        form = ConfigScriptForm(request.POST, instance=config_script)
        if form.is_valid():
            form.save()
            return redirect('manage_configs')
        else:
            alertErrors(request, form.errors)
    else:
        form = ConfigScriptForm(instance=config_script)

    context = { 
        'object_type': "Config",
        'new_object': False,
        'form': form,
        'delete_url': "delete_config",
        'object_id': id
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def newConfigScript(request):
    if not request.user.is_staff:
        return redirect('play')
    
    if request.method == "POST":
        form = ConfigScriptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_configs')
        else:
            alertErrors(request, form.errors)
    else:
        form = ConfigScriptForm()

    context = { 
        'object_type': "Config",
        'new_object': True,
        'form': form
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def deleteConfigScript(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')

    if id == -1:
        return redirect('manage_configs')

    config_script = ConfigScript.objects.get(id=id)
    if config_script is None:
        return redirect('manage_configs')

    if config_script.xas_group.umpire != request.user.assassin:
        return redirect('manage_configs')

    config_script.delete()
    return redirect('manage_configs')

####################################################################################################
####################################################################################################

@login_required(login_url='login')
def manageEventScripts(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')
    
    if id == -1:
        context = { 'events': EventScript.objects.all() }
        return render(request, 'games/manage_eventscripts.html', context)
    
    event_script = EventScript.objects.get(id=id)
    if event_script is None:
        return redirect('manage_events')

    if request.method == "POST":
        form = EventScriptForm(request.POST, instance=event_script)
        if form.is_valid():
            form.save()
            return redirect('manage_events')
        else:
            alertErrors(request, form.errors)
    else:
        form = EventScriptForm(instance=event_script)

    context = { 
        'object_type': "Event",
        'new_object': False,
        'form': form,
        'delete_url': "delete_event",
        'object_id': id
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def newEventScript(request):
    if not request.user.is_staff:
        return redirect('play')
    
    if request.method == "POST":
        form = EventScriptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_events')
        else:
            alertErrors(request, form.errors)
    else:
        form = EventScriptForm()

    context = { 
        'object_type': "Event",
        'new_object': True,
        'form': form
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def deleteEventScript(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')

    if id == -1:
        return redirect('manage_events')

    event_script = EventScript.objects.get(id=id)
    if event_script is None:
        return redirect('manage_events')

    if event_script.xas_group.umpire != request.user.assassin:
        return redirect('manage_events')

    event_script.delete()
    return redirect('manage_events')

####################################################################################################
####################################################################################################

@login_required(login_url='login')
def manageGameScripts(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')
    
    if id == -1:
        context = { 'scripts': GameScript.objects.all() }
        return render(request, 'games/manage_gamescripts.html', context)
    
    game_script = GameScript.objects.get(id=id)
    if game_script is None:
        return redirect('manage_scripts')

    if request.method == "POST":
        form = GameScriptForm(request.POST, instance=game_script)
        if form.is_valid():
            form.save()
            return redirect('manage_scripts')
        else:
            alertErrors(request, form.errors)
    else:
        form = GameScriptForm(instance=game_script)

    context = { 
        'object_type': "Script",
        'new_object': False,
        'form': form,
        'delete_url': "delete_script",
        'object_id': id
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def newGameScript(request):
    if not request.user.is_staff:
        return redirect('play')
    
    if request.method == "POST":
        form = GameScriptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_scripts')
        else:
            alertErrors(request, form.errors)
    else:
        form = GameScriptForm()

    context = { 
        'object_type': "Script",
        'new_object': True,
        'form': form
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def deleteGameScript(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')

    if id == -1:
        return redirect('manage_scripts')

    game_script = GameScript.objects.get(id=id)
    if game_script is None:
        return redirect('manage_scripts')

    if game_script.xas_group.umpire != request.user.assassin:
        return redirect('manage_scripts')

    game_script.delete()
    return redirect('manage_scripts')

####################################################################################################
####################################################################################################

@login_required(login_url='login')
def manageGames(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')

    if id == -1:
        context = { 'games': Game.objects.all() }
        return render(request, 'games/manage_games.html', context)
    
    game = Game.objects.get(id=id)
    if game is None:
        return redirect('manage_games')

    if request.method == "POST":
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('manage_games')
        else:
            alertErrors(request, form.errors)
    else:
        form = GameForm(instance=game)

    context = { 
        'object_type': "Game",
        'new_object': False,
        'form': form,
        'delete_url': "delete_game",
        'object_id': id
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def newGame(request):
    if not request.user.is_staff:
        return redirect('play')
    
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_games')
        else:
            alertErrors(request, form.errors)
    else:
        form = GameForm()

    context = { 
        'object_type': "Game",
        'new_object': True,
        'form': form
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def deleteGame(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')

    if id == -1:
        return redirect('manage_games')

    game = Game.objects.get(id=id)
    if game is None:
        return redirect('manage_games')

    if game.xas_group.umpire != request.user.assassin:
        return redirect('manage_games')

    game.delete()
    return redirect('manage_games')

####################################################################################################
####################################################################################################

@login_required(login_url='login')
def manageFlags(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')

    if id == -1:
        context = { 'flags': Flag.objects.all() }
        return render(request, 'games/manage_flags.html', context)
    
    flag = Flag.objects.get(id=id)
    if flag is None:
        return redirect('manage_flags')

    if request.method == "POST":
        form = FlagForm(request.POST, instance=flag)
        if form.is_valid():
            form.save()
            return redirect('manage_flags')
        else:
            alertErrors(request, form.errors)
    else:
        form = FlagForm(instance=flag)

    context = { 
        'object_type': "Flag",
        'new_object': False,
        'form': form,
        'delete_url': "delete_flag",
        'object_id': id
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def newFlag(request):
    if not request.user.is_staff:
        return redirect('play')
    
    if request.method == "POST":
        form = FlagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_flags')
        else:
            alertErrors(request, form.errors)
    else:
        form = FlagForm()

    context = { 
        'object_type': "Flag",
        'new_object': True,
        'form': form
    }
    return render(request, 'games/edit.html', context)

####################################################################################################

@login_required(login_url='login')
def deleteFlag(request, id=-1):
    if not request.user.is_staff:
        return redirect('play')

    if id == -1:
        return redirect('manage_flags')

    flag = Flag.objects.get(id=id)
    if flag is None:
        return redirect('manage_flags')

    if flag.xas_group.umpire != request.user.assassin:
        return redirect('manage_flags')

    flag.delete()
    return redirect('manage_flags')

####################################################################################################
####################################################################################################