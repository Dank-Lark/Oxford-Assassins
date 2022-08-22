from django.urls import path
from games import viewsplay

# Games URLs:
#   Games
#   Game by ID

urlpatterns = [
    # Play
    path('',                    viewsplay.play,            name="play"            ),
    path('signup/<int:id>/',    viewsplay.signup,          name="signup"          ),

    path('report/kill/',        viewsplay.reportKill,      name="report_kill"     ),
    path('report/death/',       viewsplay.reportDeath,     name="report_death"    ),
    path('report/set/',         viewsplay.reportSet,       name="report_set"      ),
    path('confirm/k/<int:id>/', viewsplay.confirmKill,     name="confirm_kill"    ),
    path('confirm/d/<int:id>/', viewsplay.confirmDeath,    name="confirm_death"   ),
    path('confirm/i/',          viewsplay.confirmIndirect, name="confirm_indirect"),
    path('confirm/i/<int:id>/', viewsplay.confirmIndirect                         ),

    path('players/',            viewsplay.players,         name="players"         ),
    path('players/<int:id>/',   viewsplay.players                                 ),

    path('flags/',              viewsplay.flags,           name="flags"           ),
    path('flags/<int:id>/',     viewsplay.flags                                   ),
]