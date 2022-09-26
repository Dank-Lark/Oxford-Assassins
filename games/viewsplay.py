from datetime import MAXYEAR
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from games.models import *
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
def play(request):
    '''# TODO Docstring'''

    # Check registered
    if request.user.assassin is None:
        messages.error(request, "Your account is not linked to a registered Assassin!")
        return redirect('account')
    
    # Get active/upcoming games
    active_game = None
    upcoming_games = []
    for game in Game.objects.filter(published=True):
        if game.isDuringGame(timezone.now()):
            active_game = game
            break
        if timezone.now() < game.game_start:
            upcoming_games.append(game)

    # Show upcoming games for signup, or waiting screen
    if active_game is None:
        # No games - display message
        if not upcoming_games:
            return render(request, 'games/no_games.html')

        # Get next game
        next_game = sorted(upcoming_games, key=lambda g: g.game_start)[0]

        # If already Signed Up, Show Waiting Screen, otherwise, sign up
        for player in Player.objects.filter(game=next_game):
            if player.assassin == request.user.assassin:
                # Already Signed Up, Show Waiting Screen
                context = {
                    'game_title':       next_game.title,
                    'name':             player.assassin,
                    'game_started':     False,
                    'game_start':       next_game.game_start,
                    'top_players':      Player.objects.filter(game=next_game)[:10],
                    'top_flags':        next_game.game_script.flags_used.filter(visibility=EVERYONE),
                    'lores':            None,
                    'game_description': next_game.description,
                }
                return render(request, 'games/play.html', context)
        # Not yet Signed Up, Show Sign Up Screen
        return redirect('signup', id=next_game.id)

    # Game is active - Get active player (and check respawns)
    active_player = None
    for player in Player.objects.filter(game=active_game):
        player.tryRespawn(timezone.now())
        if player.assassin == request.user.assassin:
            active_player = player

    # If not playing, spectate
    if active_player is None:
        # TODO Show spectator view
        context = {}
        return render(request, 'games/spectate.html', context)

    # Get number of respawns
    if active_game.isDuringEvent(timezone.now()):
        respawns = active_player.event_respawns
    else:
        respawns = active_player.game_respawns

    # Get confirmations to check where player is the killer
    confirmations_dk = []
    for report in DirectReport.objects.filter(killer=active_player):
        if report.didKill(active_game) and not report.killer_validated:
            confirmations_dk.append(report)

    # Get confirmations to check where player is the victim
    confirmations_dv = []
    for report in DirectReport.objects.filter(victim=active_player):
        if report.didKill(active_game) and not report.victim_validated:
            confirmations_dv.append(report)

    # Get Top Players to display
    top_players = sorted(
        Player.objects.filter( game=active_game ), 
        key=lambda p: p.totalPoints(), 
        reverse=True
    )[:10]

    # Get Top Flags to display
    top_flags = sorted(
        active_game.game_script.flags_used.filter(visibility=EVERYONE),
        key=lambda f: f.totalPoints(), 
        reverse=True
    )[:10]

    # Get visible lore to display
    lores = active_game.getInfoLore(active_player)

    context = {
        'game_title':       active_game.title,
        'name':             active_player.assassin,
        'game_started':     True,
        'game_start':       active_game.game_start,
        'alive':            active_player.alive,
        'respawns':         respawns,
        'respawn_time':     active_player.next_respawn,
        'player_flags':     active_player.flags,
        'confirmations_dk': confirmations_dk,
        'confirmations_dv': confirmations_dv,
        'top_players':      top_players,
        'top_flags':        top_flags,
        'lores':            lores,
    }
    return render(request, 'games/play.html', context)

####################################################################################################

@login_required(login_url='login')
def signup(request, id):
    '''# TODO Docstring'''

    # Get game
    try:
        game = Game.objects.get(id=id)
    except:
        return redirect('play')

    # If too late, redirect
    if not game.isAllowedSignups(timezone.now()):
        # TODO Make sure Umpires can add late arrivals manually
        return redirect('play')

    # If already signed up, redirect
    for player in Player.objects.filter(game=game):
        if player.assassin == request.user.assassin:
            return redirect('play')

    # If form submission, process
    if request.method == "POST":
        form = PlayerSignupForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.assassin = request.user.assassin
            player.game = game
            player.alive = True
            player.game_respawns = game.game_script.primary_script.respawn_count
            player.event_respawns = 0
            player.next_respawn = datetime(year=MAXYEAR, month=12, day=31)
            player.save()
            return redirect('play')
        else:
            alertErrors(request, form.errors)
    else:
        form = PlayerSignupForm()

    context = {
        'form': form,
        'game_title': game.title,
        'game_description': game.description,
    }
    return render(request, 'games/signup.html', context)

####################################################################################################

@login_required(login_url='login')
def reportKill(request):
    '''# TODO Docstring'''

    # Get active game
    active_game = None
    for game in Game.objects.filter(published=True):
        if game.isDuringGame(timezone.now()):
            active_game = game
            break

    if active_game is None:
        return redirect('play')

    # Game is active - Get active player (and check respawns)
    active_player = None
    for player in Player.objects.filter(game=active_game):
        player.tryRespawn(timezone.now())
        if player.assassin == request.user.assassin:
            active_player = player

    if active_player is None:
        return redirect('play')

    # If form submission, process
    if request.method == "POST":
        form = DirectReportKillForm(request.POST)
        if form.is_valid():
            # Save DRK Form
            report = form.save(commit=False)
            report.killer = active_player
            report.killer_validated = True
            report.save()
            # Kill Victim
            report.victim.alive = False
            report.victim.save()
            return redirect('play')
        else:
            alertErrors(request, form.errors)
    else:
        form = DirectReportKillForm()

    context = {
        'form': form,
        'headline': "Report a Kill You Made",
        'submit': "Report Kill",
    }
    return render(request, 'games/report.html', context)

####################################################################################################

@login_required(login_url='login')
def reportDeath(request):
    '''# TODO Docstring'''

    # Get active game
    active_game = None
    for game in Game.objects.filter(published=True):
        if game.isDuringGame(timezone.now()):
            active_game = game
            break

    if active_game is None:
        return redirect('play')

    # Game is active - Get active player (and check respawns)
    active_player = None
    for player in Player.objects.filter(game=active_game):
        player.tryRespawn(timezone.now())
        if player.assassin == request.user.assassin:
            active_player = player

    if active_player is None:
        return redirect('play')

    # If form submission, process
    if request.method == "POST":
        form = DirectReportDeathForm(request.POST)
        if form.is_valid():
            # Save DRK Form
            report = form.save(commit=False)
            report.victim = active_player
            report.victim_validated = True
            report.save()
            # Kill Victim (Player)
            active_player.alive = False
            active_player.save()
            return redirect('play')
        else:
            alertErrors(request, form.errors)
    else:
        form = DirectReportDeathForm()

    context = {
        'form': form,
        'headline': "Report a Death You Had",
        'submit': "Report Death",
    }
    return render(request, 'games/report.html', context)

####################################################################################################

@login_required(login_url='login')
def reportSet(request):
    '''# TODO Docstring'''

    # Get active game
    active_game = None
    for game in Game.objects.filter(published=True):
        if game.isDuringGame(timezone.now()):
            active_game = game
            break

    if active_game is None:
        return redirect('play')

    # Game is active - Get active player (and check respawns)
    active_player = None
    for player in Player.objects.filter(game=active_game):
        player.tryRespawn(timezone.now())
        if player.assassin == request.user.assassin:
            active_player = player

    if active_player is None:
        return redirect('play')

    # If form submission, process
    if request.method == "POST":
        form = IndirectReportSetForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.trapper = active_player
            report.save()
            return redirect('play')
        else:
            alertErrors(request, form.errors)
    else:
        form = IndirectReportSetForm()

    context = {
        'form': form,
        'headline': "Report a Trap You Set",
        'submit': "Set Trap",
    }
    return render(request, 'games/report.html', context)

####################################################################################################

@login_required(login_url='login')
def confirmKill(request, id):
    '''# TODO Docstring'''

    # Get death report
    try:
        report = DirectReport.objects.get(id=id)
    except:
        return redirect('play')

    # Check report pertains to you
    if report.killer.assassin != request.user.assassin:
        return redirect('play')

    # If form submission, process
    if request.method == "POST":
        form = DirectReportConfirmKillForm(request.POST)
        if form.is_valid():
            confirmation = form.save(commit=False)
            confirmation.killer_validated = True
            confirmation.save()
            return redirect('play')
        else:
            alertErrors(request, form.errors)
    else:
        form = DirectReportConfirmKillForm()

    context = {
        'form': form,
        'headline': "Confirm a Kill You Made",
        'submit': "Confirm Kill",
    }
    return render(request, 'games/report.html', context)

####################################################################################################

@login_required(login_url='login')
def confirmDeath(request, id):
    '''# TODO Docstring'''

    # Get death report
    try:
        report = DirectReport.objects.get(id=id)
    except:
        return redirect('play')

    # Check report pertains to you
    if report.victim.assassin != request.user.assassin:
        return redirect('play')

    # If form submission, process
    if request.method == "POST":
        form = DirectReportConfirmDeathForm(request.POST)
        if form.is_valid():
            confirmation = form.save(commit=False)
            confirmation.victim_validated = True
            confirmation.save()
            return redirect('play')
        else:
            alertErrors(request, form.errors)
    else:
        form = DirectReportConfirmDeathForm()

    context = {
        'form': form,
        'headline': "Confirm a Death You Had",
        'submit': "Confirm Death",
    }
    return render(request, 'games/report.html', context)

####################################################################################################

@login_required(login_url='login')
def confirmIndirect(request, id=-1):
    '''# TODO Docstring'''

    # If no trap specified
    if id == -1:
        # Get active game
        active_game = None
        for game in Game.objects.filter(published=True):
            if game.isDuringGame(timezone.now()):
                active_game = game
                break

        if active_game is None:
            return redirect('play')

        # Game is active - Get active player (and check respawns)
        active_player = None
        for player in Player.objects.filter(game=active_game):
            player.tryRespawn(timezone.now())
            if player.assassin == request.user.assassin:
                active_player = player

        if active_player is None:
            return redirect('play')

        context = {
            'traps': IndirectReport.objects.filter(target=active_player, trap_sprung=False)
        }
        return render(request, 'games/confirm_list.html', context)

    # Trap ID Specified, get associated trap
    try:
        report = IndirectReport.objects.get(id=id)
    except:
        return redirect('play')

    # Check report pertains to you
    if report.target.assassin != request.user.assassin:
        return redirect('play')

    # If form submission, process
    if request.method == "POST":
        form = IndirectReportSpringForm(request.POST)
        if form.is_valid():
            confirmation = form.save(commit=False)
            confirmation.trap_sprung = True
            confirmation.save()
            return redirect('play')
        else:
            alertErrors(request, form.errors)
    else:
        form = IndirectReportSpringForm()

    context = {
        'form': form,
        'headline': "Confirm a Trap You Sprung",
        'submit': "Spring Trap",
    }
    return render(request, 'games/report.html', context)

####################################################################################################

@login_required(login_url='login')
def players(request, id=-1):
    pass

####################################################################################################

@login_required(login_url='login')
def flags(request, id=-1):
    pass

####################################################################################################
####################################################################################################
####################################################################################################

def getUmpireGame():
    upcoming_games = []
    for game in Game.objects.filter(published=True):
        if game.isDuringGame(timezone.now()):
            return game
        if timezone.now() < game.game_start:
            upcoming_games.append(game)

    if not upcoming_games:
        return None

    return sorted(upcoming_games, key=lambda g: g.game_start)[0]

####################################################################################################

@login_required(login_url='login')
def umpire(request):
    game = getUmpireGame()
    if game is None:
        return redirect('play')

    if request.user.assassin != game.xas_group.umpire:
        return redirect('play')

    for player in Player.objects.filter(game=game):
        player.tryRespawn(timezone.now())

    context = {
        # TODO context
    }
    # TODO umpire.html
    return render(request, 'games/umpire.html', context)

####################################################################################################

@login_required(login_url='login')
def umpireReports(request):
    game = getUmpireGame()
    if game is None:
        return redirect('play')

    if request.user.assassin != game.xas_group.umpire:
        return redirect('play')

    context = {
        # TODO context
    }
    # TODO umpire_reports.html
    return render(request, 'games/umpire_reports.html', context)

####################################################################################################
         
@login_required(login_url='login')
def umpireDirectReports(request, id=-1):
    game = getUmpireGame()
    if game is None:
        return redirect('play')

    if request.user.assassin != game.xas_group.umpire:
        return redirect('play')

    if id == -1:
        context = {
            # TODO context
        }
        # TODO umpire_direct_reports.html
        return render(request, 'games/umpire_direct_reports.html', context)

    try:
        report = DirectReport.objects.get(id=id)
    except:
        return redirect('umpire_direct_reports')

    if request.method == "POST":
        form = DirectReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
        else:
            alertErrors(request, form.errors)
        return redirect('umpire_direct_reports')
    else:
        form = DirectReportForm(instance=report)
        context = {
            # TODO context
        }
        # TODO umpire_form.html
        return render(request, 'games/umpire_form.html', context)

####################################################################################################
         
@login_required(login_url='login')
def umpireIndirectReports(request, id=-1):
    game = getUmpireGame()
    if game is None:
        return redirect('play')

    if request.user.assassin != game.xas_group.umpire:
        return redirect('play')

    if id == -1:
        context = {
            # TODO context
        }
        # TODO umpire_indirect_reports.html
        return render(request, 'games/umpire_indirect_reports.html', context)

    try:
        report = IndirectReport.objects.get(id=id)
    except:
        return redirect('umpire_indirect_reports')
        
    if request.method == "POST":
        form = IndirectReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
        else:
            alertErrors(request, form.errors)
        return redirect('umpire_indirect_reports')
    else:
        form = IndirectReportForm(instance=report)
        context = {
            # TODO context
        }
        # TODO umpire_form.html
        return render(request, 'games/umpire_form.html', context)

####################################################################################################
         
@login_required(login_url='login')
def umpireGeneralReports(request, id=-1):
    game = getUmpireGame()
    if game is None:
        return redirect('play')

    if request.user.assassin != game.xas_group.umpire:
        return redirect('play')

    if id == -1:
        context = {
            # TODO context
        }
        # TODO umpire_general_reports.html
        return render(request, 'games/umpire_general_reports.html', context)

    try:
        report = GeneralReport.objects.get(id=id)
    except:
        return redirect('umpire_general_reports')
        
    if request.method == "POST":
        form = GeneralReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
        else:
            alertErrors(request, form.errors)
        return redirect('umpire_general_reports')
    else:
        form = GeneralReportForm(instance=report)
        context = {
            # TODO context
        }
        # TODO umpire_form.html
        return render(request, 'games/umpire_form.html', context)

####################################################################################################
         
@login_required(login_url='login')
def umpirePlayerBonus(request, id=-1):
    game = getUmpireGame()
    if game is None:
        return redirect('play')

    if request.user.assassin != game.xas_group.umpire:
        return redirect('play')

    if id == -1:
        context = {
            # TODO context
        }
        # TODO umpire_player_bonus.html
        return render(request, 'games/umpire_player_bonus.html', context)

    try:
        bonus = PlayerBonus.objects.get(id=id)
    except:
        return redirect('umpire_player_bonus')
        
    if request.method == "POST":
        form = PlayerBonusForm(request.POST, instance=bonus)
        if form.is_valid():
            form.save()
        else:
            alertErrors(request, form.errors)
        return redirect('umpire_player_bonus')
    else:
        form = PlayerBonusForm(instance=bonus)
        context = {
            # TODO context
        }
        # TODO umpire_form.html
        return render(request, 'games/umpire_form.html', context)

####################################################################################################
         
@login_required(login_url='login')
def umpirePlayerBonusNew(request):
    game = getUmpireGame()
    if game is None:
        return redirect('play')

    if request.user.assassin != game.xas_group.umpire:
        return redirect('play')

    if request.method == "POST":
        form = PlayerBonusForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            alertErrors(request, form.errors)
        return redirect('umpire_player_bonus')
    else:
        form = PlayerBonusForm()
        context = {
            # TODO context
        }
        # TODO umpire_form.html
        return render(request, 'games/umpire_form.html', context)

####################################################################################################
         
@login_required(login_url='login')
def umpirePlayerBonusDelete(request, id=-1):
    game = getUmpireGame()
    if game is None:
        return redirect('play')

    if request.user.assassin != game.xas_group.umpire:
        return redirect('play')

    try:
        bonus = PlayerBonus.objects.get(id=id)
    except:
        return redirect('umpire_player_bonus')

    bonus.delete()
    return redirect('umpire_player_bonus')

####################################################################################################
         
@login_required(login_url='login')
def umpireFlagBonus(request, id=-1):
    game = getUmpireGame()
    if game is None:
        return redirect('play')

    if request.user.assassin != game.xas_group.umpire:
        return redirect('play')

    if id == -1:
        context = {
            # TODO context
        }
        # TODO umpire_player_bonus.html
        return render(request, 'games/umpire_flag_bonus.html', context)

    try:
        bonus = FlagBonus.objects.get(id=id)
    except:
        return redirect('umpire_flag_bonus')
        
    if request.method == "POST":
        form = FlagBonusForm(request.POST, instance=bonus)
        if form.is_valid():
            form.save()
        else:
            alertErrors(request, form.errors)
        return redirect('umpire_flag_bonus')
    else:
        form = FlagBonusForm(instance=bonus)
        context = {
            # TODO context
        }
        # TODO umpire_form.html
        return render(request, 'games/umpire_form.html', context)

####################################################################################################
         
@login_required(login_url='login')
def umpireFlagBonusNew(request):
    game = getUmpireGame()
    if game is None:
        return redirect('play')

    if request.user.assassin != game.xas_group.umpire:
        return redirect('play')

    if request.method == "POST":
        form = FlagBonusForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            alertErrors(request, form.errors)
        return redirect('umpire_flag_bonus')
    else:
        form = FlagBonusForm()
        context = {
            # TODO context
        }
        # TODO umpire_form.html
        return render(request, 'games/umpire_form.html', context)

####################################################################################################
         
@login_required(login_url='login')
def umpireFlagBonusDelete(request, id=-1):
    game = getUmpireGame()
    if game is None:
        return redirect('play')

    if request.user.assassin != game.xas_group.umpire:
        return redirect('play')

    try:
        bonus = FlagBonus.objects.get(id=id)
    except:
        return redirect('umpire_flag_bonus')

    bonus.delete()
    return redirect('umpire_flag_bonus')

####################################################################################################
         
@login_required(login_url='login')
def umpireBounty(request, id=-1):
    game = getUmpireGame()
    if game is None:
        return redirect('play')

    if request.user.assassin != game.xas_group.umpire:
        return redirect('play')

    if id == -1:
        context = {
            # TODO context
        }
        # TODO umpire_bounty.html
        return render(request, 'games/umpire_bounty.html', context)

    try:
        bounty = PlayerBounty.objects.get(id=id)
    except:
        return redirect('umpire_bounty')
        
    if request.method == "POST":
        form = PlayerBountyForm(request.POST, instance=bounty)
        if form.is_valid():
            form.save()
        else:
            alertErrors(request, form.errors)
        return redirect('umpire_bounty')
    else:
        form = PlayerBountyForm(instance=bounty)
        context = {
            # TODO context
        }
        # TODO umpire_form.html
        return render(request, 'games/umpire_form.html', context)


####################################################################################################
         
@login_required(login_url='login')
def umpireBountyNew(request):
    game = getUmpireGame()
    if game is None:
        return redirect('play')

    if request.user.assassin != game.xas_group.umpire:
        return redirect('play')

    if request.method == "POST":
        form = PlayerBountyForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            alertErrors(request, form.errors)
        return redirect('umpire_bounty')
    else:
        form = PlayerBountyForm()
        context = {
            # TODO context
        }
        # TODO umpire_form.html
        return render(request, 'games/umpire_form.html', context)

####################################################################################################
         
@login_required(login_url='login')
def umpireBountyDelete(request, id=-1):
    game = getUmpireGame()
    if game is None:
        return redirect('play')

    if request.user.assassin != game.xas_group.umpire:
        return redirect('play')

    try:
        bonus = PlayerBounty.objects.get(id=id)
    except:
        return redirect('umpire_bounty')

    bonus.delete()
    return redirect('umpire_bounty')

####################################################################################################
         
@login_required(login_url='login')
def umpirePlayers(request, id=-1):
    game = getUmpireGame()
    if game is None:
        return redirect('play')

    if request.user.assassin != game.xas_group.umpire:
        return redirect('play')

    if id == -1:
        context = {
            # TODO context
        }
        # TODO umpire_players.html
        return render(request, 'games/umpire_players.html', context)

    try:
        player = Player.objects.get(id=id)
    except:
        return redirect('umpire_players')

    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
        else:
            alertErrors(request, form.errors)
        return redirect('umpire_players')
    else:
        form = PlayerForm(instance=player)
        context = {
            # TODO context
        }
        # TODO umpire_form.html
        return render(request, 'games/umpire_form.html', context)
 
####################################################################################################
         
@login_required(login_url='login')
def umpireFlags(request, id=-1):
    game = getUmpireGame()
    if game is None:
        return redirect('play')

    if request.user.assassin != game.xas_group.umpire:
        return redirect('play')

    if id == -1:
        context = {
            # TODO context
        }
        # TODO umpire_flags.html
        return render(request, 'games/umpire_flags.html', context)

    try:
        flag = Flag.objects.get(id=id)
    except:
        return redirect('umpire_flags')

    if request.method == "POST":
        form = FlagForm(request.POST, instance=flag)
        if form.is_valid():
            form.save()
        else:
            alertErrors(request, form.errors)
        return redirect('umpire_flags')
    else:
        form = FlagForm(instance=flag)
        context = {
            # TODO context
        }
        # TODO umpire_form.html
        return render(request, 'games/umpire_form.html', context)
             