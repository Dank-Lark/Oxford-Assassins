from django.urls import path
from . import views

# Games URLs:
#   Games
#   Game by ID

urlpatterns = [
    # Manage
    path('',                        views.manage,              name="manage"),

    path('games/',                  views.manageGames,         name="manage_games"),
    path('games/<int:id>/',         views.manageGames),
    path('games/new/',              views.newGame,             name="new_game"),

    path('flags/',                  views.manageFlags,         name="manage_flags"),
    path('flags/<int:id>/',         views.manageFlags),
    path('flags/new/',              views.newFlag,             name="new_flag"),

    path('gamescripts/',            views.manageGameScripts,   name="manage_scripts"),
    path('gamescripts/<int:id>/',   views.manageGameScripts),
    path('gamescripts/new/',        views.newGameScript,       name="new_script"),

    path('eventscripts/',           views.manageEventScripts,  name="manage_events"),
    path('eventscripts/<int:id>/',  views.manageEventScripts),
    path('eventscripts/new/',       views.newEventScript,      name="new_event"),

    path('configscripts/',          views.manageConfigScripts, name="manage_configs"),
    path('configscripts/<int:id>/', views.manageConfigScripts),
    path('configscripts/new/',      views.newConfigScript,     name="new_config"),
]