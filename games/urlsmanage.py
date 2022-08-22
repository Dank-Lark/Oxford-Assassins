from django.urls import path
from games import viewsmanage

# Games URLs:
#   Games
#   Game by ID

urlpatterns = [
    # Manage
    path('',                              viewsmanage.manage,              name="manage"),

    path('groups/',                       viewsmanage.manageXASGroups,     name="manage_groups"),
    path('groups/<int:id>/',              viewsmanage.manageXASGroups),
    path('groups/new/',                   viewsmanage.newXASGroup,         name="new_group"),
    path('groups/delete/<int:id>',        viewsmanage.deleteXASGroup,      name="delete_group"),

    path('configscripts/',                viewsmanage.manageConfigScripts, name="manage_configs"),
    path('configscripts/<int:id>/',       viewsmanage.manageConfigScripts),
    path('configscripts/new/',            viewsmanage.newConfigScript,     name="new_config"),
    path('configscripts/delete/<int:id>', viewsmanage.deleteConfigScript,  name="delete_config"),

    path('eventscripts/',                 viewsmanage.manageEventScripts,  name="manage_events"),
    path('eventscripts/<int:id>/',        viewsmanage.manageEventScripts),
    path('eventscripts/new/',             viewsmanage.newEventScript,      name="new_event"),
    path('eventscripts/delete/<int:id>',  viewsmanage.deleteEventScript,   name="delete_event"),

    path('gamescripts/',                  viewsmanage.manageGameScripts,   name="manage_scripts"),
    path('gamescripts/<int:id>/',         viewsmanage.manageGameScripts),
    path('gamescripts/new/',              viewsmanage.newGameScript,       name="new_script"),
    path('gamescripts/delete/<int:id>',   viewsmanage.deleteGameScript,    name="delete_script"),

    path('games/',                        viewsmanage.manageGames,         name="manage_games"),
    path('games/<int:id>/',               viewsmanage.manageGames),
    path('games/new/',                    viewsmanage.newGame,             name="new_game"),
    path('games/delete/<int:id>',         viewsmanage.deleteGame,          name="delete_game"),

    path('flags/',                        viewsmanage.manageFlags,         name="manage_flags"),
    path('flags/<int:id>/',               viewsmanage.manageFlags),
    path('flags/new/',                    viewsmanage.newFlag,             name="new_flag"),
    path('flags/delete/<int:id>',         viewsmanage.deleteFlag,          name="delete_flag"),

    path('infolore/',                     viewsmanage.manageInfoLore,      name="manage_infolore"),
    path('infolore/<int:id>/',            viewsmanage.manageInfoLore),
    path('infolore/new/',                 viewsmanage.newInfoLore,         name="new_infolore"),
    path('infolore/delete/<int:id>',      viewsmanage.deleteInfoLore,      name="delete_infolore"),
]