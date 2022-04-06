from urllib import request
from django.shortcuts import render

# Play Views:
#   play_overview
#   play_events_list
#   play_event
#   play_map
#   play_report
#   play_stats
#   play_user_stats
#   play_teams

def overview(request):
    context = {}
    return render(request, 'play/play_overview.html', context)

def eventsList(request):
    context = {}
    return render(request, 'play/play_events_list.html', context)

def event(request):
    context = {}
    return render(request, 'play/play_event.html', context)

def map(request):
    context = {}
    return render(request, 'play/play_map.html', context)

def report(request):
    context = {}
    return render(request, 'play/play_report.html', context)

def stats(request):
    context = {}
    return render(request, 'play/play_stats.html', context)

def userStats(request):
    context = {}
    return render(request, 'play/play_user_stats.html', context)

def teams(request):
    context = {}
    return render(request, 'play/play_teams.html', context)