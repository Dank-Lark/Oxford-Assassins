from django.urls import path
from games import viewsplay

# Games URLs:
#   Games
#   Game by ID

urlpatterns = [
    # Play     
    path('',                                viewsplay.play,                    name="play"                      ),
    path('signup/<int:id>/',                viewsplay.signup,                  name="signup"                    ),
                              
    path('report/kill/',                    viewsplay.reportKill,              name="report_kill"               ),
    path('report/death/',                   viewsplay.reportDeath,             name="report_death"              ),
    path('report/set/',                     viewsplay.reportSet,               name="report_set"                ),
    path('confirm/k/<int:id>/',             viewsplay.confirmKill,             name="confirm_kill"              ),
    path('confirm/d/<int:id>/',             viewsplay.confirmDeath,            name="confirm_death"             ),
    path('confirm/i/',                      viewsplay.confirmIndirect,         name="confirm_indirect"          ),
    path('confirm/i/<int:id>/',             viewsplay.confirmIndirect                                           ),
                              
    path('players/',                        viewsplay.players,                 name="players"                   ),
    path('players/<int:id>/',               viewsplay.players                                                   ),
                           
    path('flags/',                          viewsplay.flags,                   name="flags"                     ),
    path('flags/<int:id>/',                 viewsplay.flags                                                     ),
                      
    # Umpire         
    path('umpire/',                         viewsplay.umpire,                  name="umpire"                    ),
    path('umpire/reports/',                 viewsplay.umpireReports,           name="umpire_reports"            ),
         
    path('umpire/reports/d/',               viewsplay.umpireDirectReports,     name="umpire_direct_reports"     ),
    path('umpire/reports/d/<int:id>/',      viewsplay.umpireDirectReports                                       ),
    path('umpire/reports/i/',               viewsplay.umpireIndirectReports,   name="umpire_indirect_reports"   ),
    path('umpire/reports/i/<int:id>/',      viewsplay.umpireIndirectReports                                     ),
    path('umpire/reports/g/',               viewsplay.umpireGeneralReports,    name="umpire_general_reports"    ),
    path('umpire/reports/g/<int:id>/',      viewsplay.umpireGeneralReports                                      ),
        
    path('umpire/bonus/p/',                 viewsplay.umpirePlayerBonus,       name="umpire_player_bonus"       ),
    path('umpire/bonus/p/<int:id>/',        viewsplay.umpirePlayerBonus                                         ),    
    path('umpire/bonus/p/new/',             viewsplay.umpirePlayerBonusNew,    name="umpire_new_player_bonus"   ),
    path('umpire/bonus/p/delete/<int:id>/', viewsplay.umpirePlayerBonusDelete, name="umpire_delete_player_bonus"),

    path('umpire/bonus/f/',                 viewsplay.umpireFlagBonus,         name="umpire_flag_bonus"         ),
    path('umpire/bonus/f/<int:id>/',        viewsplay.umpireFlagBonus                                           ),
    path('umpire/bonus/f/new/',             viewsplay.umpireFlagBonusNew,      name="umpire_new_flag_bonus"     ),
    path('umpire/bonus/f/delete/<int:id>/', viewsplay.umpireFlagBonusDelete,   name="umpire_delete_flag_bonus"  ),
     
    path('umpire/bounty/',                  viewsplay.umpireBounty,            name="umpire_bounty"             ),
    path('umpire/bounty/<int:id>/',         viewsplay.umpireBounty                                              ),
    path('umpire/bounty/new/',              viewsplay.umpireBountyNew,         name="umpire_new_bounty"         ),
    path('umpire/bounty/delete/<int:id>/',  viewsplay.umpireBountyDelete,      name="umpire_delete_bounty"      ),
   
    path('umpire/players/',                 viewsplay.umpirePlayers,           name="umpire_players"            ),
    path('umpire/players/<int:id>/',        viewsplay.umpirePlayers                                             ),
   
    path('umpire/flags/',                   viewsplay.umpireFlags,             name="umpire_flags"              ),
    path('umpire/flags/<int:id>/',          viewsplay.umpireFlags                                               ),
]