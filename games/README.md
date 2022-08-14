# models.py - database
| Model | Description |
| - | - |
| XASGroup | Administrative details for a group of models. |
| Flag | Represents teams, status effects, etc. |
| InfoLore | Information or lore text to be released to players at a given time. |
| ConfigScript | Configuration details for an event or game. |
| EventScript | ConfigScript with offset timing for an event in a game. |
| GameScript | A primary ConfigScript and a selection of EventScripts. |
| Game | Information about a game, a script, and timing. |
| Player | Connects an Assassin to a Game and holds in-game data about them. |
| DirectReport | A report of a kill or death. |
| IndirectReport | A report of a trap being laid or sprung. |
| GeneralReport | A non-kill/death/indirect report. |
| PlayerBonus | Assign bonus points to players. |
| FlagBonus | Assign bonus points to flags. |
---
| XASGroup | Administrative details for a group of models.|
| - | - |
| umpire | Which umpire owns this group? |
| reference | The group reference or display name for the group. |
| created | The date this group was created. |

| Flag | Represents teams, status effects, etc. |
| - | - |
| xas_group | Which group of models does this Flag belong to? |
| name | The display name for the flag. |
| visibility | Who can see this flag attatched to a player. |
| friendly | Players sharing this flag have friendly-fire disabled. |         
| allowed_melee | Is a kill with a melee weapon allowed? |
| allowed_thrown | Is a kill with a thrown weapon allowed? |
| allowed_ranged | Is a kill with a ranged weapon allowed? |
| allowed_animal | Is a kill with an attack animal allowed? |
| allowed_costume | Is a kill with a costume allowed? |
| multiplier_melee | How much to multiply the score of melee kills by? |
| multiplier_thrown | How much to multiply the score of thrown kills by? |
| multiplier_ranged | How much to multiply the score of ranged kills by? |
| multiplier_animal | How much to multiply the score of animal kills by? |
| multiplier_costume | How much to multiply the score of costume kills by? |
| bonus_melee | How many bonus points to award kills by melee weapons. |
| bonus_thrown | How many bonus points to award kills by thrown weapons. |
| bonus_ranged | How many bonus points to award kills by ranged weapons. |
| bonus_animal | How many bonus points to award kills by attack animals. |
| bonus_costume | How many bonus points to award kills by costumes. |
| allowed_normal | Is a normal kill valid? |
| allowed_raid | Is a kill in a raid valid? |
| allowed_duel | Is a kill in a duel valid? |
| multiplier_normal | How much to multiply the score of normal kills by? |
| multiplier_raid | How much to multiply the score of kills in a raid by? |
| multiplier_duel | How much to multiply the score of kills in a duel by? |
| bonus_normal | How many bonus points to award normal kills. |
| bonus_raid | How many bonus points to award kills in a raid. |
| bonus_duel | How many bonus points to award kills in a duel. |
| allowed_indirect | Are indirect kills valid? |
| multiplier_indirect | How much to multiply the score of indirect kills by? |
| bonus_indirect | How many bonus points to award indirect kills? |   
| on_kill | How should flag transfers be handled when the player kills? |
| on_death | How should flag transfers be handled when the player dies? |

| InfoLore | Information or lore text to be released to players at a given time. |
| - | - |
| xas_group | Which group of models does this InfoLore belong to? |
| title | The title of the information or lore release. |
| text | The main text body of the release. |
| media | Supplimentary media included in the release. |
| release_start | When is the info or lore released? |
| release_end | When is the info or lore removed? |
| public | Is this visible to all players? |
| flags | If not public, who can see the release? |

| ConfigScript | Configuration details for an event or game. |
| - | - |
| xas_group | Which group of models does this ConfigScript belong to? |
| config_name | The display name for a configuration |
| allowed_melee | Is a kill with a melee weapon allowed? |
| allowed_thrown | Is a kill with a thrown weapon allowed? |
| allowed_ranged | Is a kill with a ranged weapon allowed? |
| allowed_animal | Is a kill with an attack animal allowed? |
| allowed_costume | Is a kill with a costume allowed? |
| points_melee | How many points is a kill with a melee weapon worth? |
| points_thrown | How many points is a kill with a thrown weapon worth? |
| points_ranged | How many points is a kill with a ranged weapon worth? |
| points_animal | How many points is a kill with an attack animal worth? |
| points_costume | How many points is a kill with a costume worth? |
| allowed_normal | Is a normal kill valid? |
| allowed_raid | Is a kill in a raid valid? |
| allowed_duel | Is a kill in a duel valid? |
| points_normal | How many points is a normal kill worth? |
| points_raid | How many points is a kill in a raid worth? |
| points_duel | How many points is a kill in a duel worth? |
| allowed_indirect | Is an indirect kill allowed? |          
| points_indirect | How many points is an indirect kill worth? | 
| respawn_count | How many respawns are allowed while this config is active? |
| respawn_time | How long between a death and a respawn? |
| respawn_start | Should there be a global respawn at the start of this event? |
| respawn_end | Should there be a global respawn at the end of this event? |
| respawn_delay | How long after the event ends before global respawn? |
| protect_flags | Should flag transfers be prohibited in this config? |

| EventScript | ConfigScript with offset timing for an event in a game. |
| - | - |
| xas_group | Which group of models does this EventScript belong to? |
| event_config | The ConfigScript to refer to for rules in this event. |
| event_start | When to start the event. |
| event_duration | How long is this event? |

| GameScript | A primary ConfigScript and a selection of EventScripts. |
| - | - |
| xas_group | Which group of models does this GameScript belong to? |
| primary_script | The primary configuration for the game. |
| event_scripts | Override scripts and timing for events during the game. |
| info_lore_releases | List of InfoLore releases to be included in the game. |

| Game | Information about a game, a script, and timing. |
| - | - |
| xas_group | Which group of models does this Game belong to? |
| title | The display name for the game. |         
| description | The description for the game. |   
| game_script | The GameScript that defines the rules of the game. |   
| game_start | The date and time for the game to begin. |     
| game_duration | The length of time from start to end of the game. |

| Player | Connects an Assassin to a Game and holds in-game data about them. |
| - | - |
| assassin | The assassin connected to this player. |
| game | The game connected to this player. |
| is_alive | Is the player currently alive? |
| game_respawns | How many respawns this player has left in the game? | 
| event_respawns | How many respawns this player has left in the event? |
| next_respawn | When does the player next respawn?
| flags | The flags the player has. |

| DirectReport | A report of a kill or death. |
| - | - |
| killer | The player reporting their kill. |
| victim | The player reporting their death. |
| weapon | Melee, Thrown, Ranged, Attack Animal, or Costume. |
| context | Normal, Raid, or Duel. |
| location | Where the kill took place. |
| date | The date and time of the kill. |
| killer_report | The report text written by the killer. |
| victim_report | The report text written by the victim. |
| killer_media | Supplimentary media added by the killer. |
| victim_media | Supplimentary media added by the victim. |
| killer_validated | Does the killer agree this kill occured? |
| victim_validated | Does the victim agree this kill occured? |
| confirm_date | When was this report validated? |

| IndirectReport | A report of a trap being laid or sprung. |
| - | - |
| trapper | The player who laid the trap. |        
| target | The player who sprung the trap. |         
| location | Where the trap was set. |       
| date_set | When the trap was set. |       
| date_sprung | When the trap was sprung. |    
| trapper_report | The report text written by the trapper. | 
| target_report | The report text written by the target. |  
| trapper_media | Supplimentary media added by the trapper. |
| target_media | Supplimentary media added by the target. | 
| trap_sprung | Has the trap been sprung yet? |    
| trap_successful | When the trap sprung, was it sucessful? |

| GeneralReport | A non-kill/death/indirect report. |
| - | - |
| player | The player making the report. |
| location | Where the report comes from. |
| date | When the report was made. |
| report_text | The report text written by the player. |
| report_media | Supplimentary media added by the player. |

| PlayerBonus | Assign bonus points to players. |
| - | - |
| player | The player being given the bonus. |
| date | When the bonus was given. |
| points | How many points to award. |

| TeamBonus | Assign bonus points to flags. |
| - | - |
| flags | The flags being given the bonus. |
| date | When the bonus was given. |
| points | How many points to award. |

---
<br>

# models.py - functions
| Model | Function | Takes | Returns | Effects |
| - | - | - | - | - |
| ConfigScript | _isWeaponAllowed | report | bool: is weapon allowed? | Switches against MELEE, THROWN, RANGED, ANIMAL, or COSTUME. |
| | _getWeaponScore | report | int: points awarded for use of weapon? | Switches against MELEE, THROWN, RANGED, ANIMAL, or COSTUME. |
| | _isContextAllowed | report | bool: is kill context allowed? | Switches against NORMAL, RAID, or DUEL. |
| | _getContextScore | report | int: points awarded for kill in this context? | Switches against NORMAL, RAID, or DUEL. |
| | isKillAllowed | report | bool: is weapon used and kill context allowed? | Calls _isWeaponAllowed and _isContextAllowed. |
| | getKillScore | report | int: points awarded for use of weapon in this context? | Calls _getWeaponScore and _getContextScore. |
| EventScript | isDuringEvent | game_time | bool: Is game_time during this event? | Compares against event_start and event_duration. |
| GameScript | isDuringEvent | game_time | bool: Is game_time during an event? | Calls isDuringEvent on each attatched EventScript. |
| | getConfig | game_time | ConfigScript: The configuration of the active event, or primary script. | Calls isDuringEvent on each attatched EventScript. |
| Game | isDuringGame | time | bool: Is this game active at the given time? | Compares against game_start and game_duration. |
| | isDuringEvent | time | bool: Is time during an event? | Converts time to game_time and calls isDuringEvent on game_script. |
| | getConfig | time | ConfigScript: The configuration of the active event, or primary script. | Converts time to game_time and calls getConfig on game_script. |
| Flag | _isWeaponAllowed | report | bool: Does this flag allow this weapon? | Switches against MELEE, THROWN, RANGED, ANIMAL, or COSTUME. |
| | _getWeaponMultiplier | report | bool: How much does this flag multiply points for this weapon by? | Switches against MELEE, THROWN, RANGED, ANIMAL, or COSTUME. |
| | _getWeaponBonus | report | bool: How many bonus points does this flag award this weapon? | Switches against MELEE, THROWN, RANGED, ANIMAL, or COSTUME. |
| | _isContextAllowed | report | bool: Does this flag allow this context? | Switches against NORMAL, RAID, or DUEL. |
| | _getContextMultiplier | report | bool: How much does this flag multiply points for this context by? | Switches against NORMAL, RAID, or DUEL. |
| | _getContextBonus | report | bool: How many bonus points does this flag award this context? | Switches against NORMAL, RAID, or DUEL. |
| | isKillAllowed | report | bool: Does this flag allow this kill? | Calls _isWeaponAllowed and _isContextAllowed. |
| | getKillMultiplier | report | bool: How much does this flag multiply points for this kill by? | Calls _getWeaponMultiplier and _getContextMultiplier. |
| | getKillBonus | report | bool: How many bonus points does this flag award this kill? | Calls _getWeaponBonus and _getContextBonus. |
| Player | tryRespawn | time | bool: Was allowed to respawn? | Checks respawn conditions are valid, and if so, respawns them. |
| DirectReport | _isValid | game | bool: Is the kill valid? | Checks players are in the same game and kill happened within game timeframe. |
| | _isAllowed | | bool: Do the script and flags agree to the kill? | Checks Config and Flags allow kill, and players don't share a friendly flag. |
| | _isAgreed | | bool: Do both players agree to the kill? | Checks killer_validated and victim_validated. |
| | didKill | game | bool: Does the report constitute a kill? | Calls _isValid and _isAllowed |
| | getPoints | game | int: How many points to give the killer? | Calls didKill, _isAgreed, and getConfig.getKillScore, then collates the multipliers and bonuses over all flags and calculates total points. |
| IndirectReport | _isValid | game | bool: Is the trap valid? | Checks players are in the same game and trap set and sprung within game timeframe. |
| | _isAllowed | | bool: Does the script and agree to the trap? | Checks Config and Flags allow kill, and players don't share a friendly flag. |
| | _isAgreed | | bool: Did the trap spring and successfully kill? | Checks trap_sprung and trap_successful. |
| | didKill | game | bool: Does the report constitute a kill? | Calls _isValid, _isAllowed, and _is_agreed |
| | getPoints | game | int: How many points to give the killer? | Calls didKill, and getConfig.points_indirect, then collates the multipliers and bonuses over all flags and calculates total points. |
| GeneralReport | | | | |

---
<br>




# Triggers
| Trigger | Description | Effect |
| - | - | - |
| onGameStart | Called when game is submitted to scheduler. | ??? |
| onGameEnd | Called when the game ends. | Evaluates Winners and assigns awards. |
| onEventStart | Called when event begins. | Deals with global respawns and total lives left. |
| onEventEnd | Called when event ends. | Deals with with global respawns and total lives left.
| onKillReported |  |
| onKillConfirmed |  |
| onIndirectSet |  |
| onIndirectSprung |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |



# Stuff


Is a direct kill valid? (should the system consider the victim dead)
    # Players are in the same game          # report.isValid()
    # Kill happened within game timeframe   # report.isValid()
    # Current Config allows kill            # report.isAllowed()
    # Killer Flags all allow kill           # report.isAllowed()
    # Players don't share a friendly flag   # report.isAllowed()
Is a direct kill agreed? (should the system award the killer points)


A direct kill will 
#Todo - Add Functions
#Todo - Add Event Win Conditions
#Todo - Add Event Win Rewards
#Todo - Add Interfaces
    # - Report kill
    # - Prompt to validate kill
    # - Validate kill
    # - Plant trap
    # - Spring trap