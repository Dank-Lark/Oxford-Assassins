from datetime import datetime, timedelta
from django.db import models
from account.models import Assassin

MELEE    = "MEL"
THROWN   = "THR"
RANGED   = "RNG"
ANIMAL   = "ATK"
COSTUME  = "COS"
KILL_METHODS = [
    (MELEE,    "Melee"),
    (THROWN,   "Thrown"),
    (RANGED,   "Ranged"),
    (ANIMAL,   "Attack Animal"),
    (COSTUME,  "Costume"),
]

NORMAL = "NOR"
RAID   = "RAD"
DUEL   = "DUL"
KILL_CONTEXTS = [
    (NORMAL, "Normal"),
    (RAID,   "Raid"),
    (DUEL,   "Duel"),
]

KEEP          = "KNP"
LOSE          = "LNP"
KEEP_AND_PASS = "KAP"
LOSE_AND_PASS = "LAP"
FLAG_TRANSFER = [
    (KEEP,          "Keep"),
    (LOSE,          "Lose"),
    (KEEP_AND_PASS, "Keep and Pass"),
    (LOSE_AND_PASS, "Lose and Pass"),
]

EVERYONE = "EVR"
SHARED   = "SHR"
HIDDEN   = "HID"
FLAG_VISIBILITY = [
    (EVERYONE, "Everyone"),
    (SHARED,   "Shared"),
    (HIDDEN,   "Hidden"),
]

####################################################################################################

class ConfigScript(models.Model):
    '''Configuration details for an event or game.'''

    # General Configuration
    config_name      = models.CharField("config name", max_length=100)

    # Weaponry Scoring Rules    
    allowed_melee    = models.BooleanField("allow melee",                      default=True)
    allowed_thrown   = models.BooleanField("allow thrown",                     default=True)
    allowed_ranged   = models.BooleanField("allow ranged",                     default=True)
    allowed_animal   = models.BooleanField("allow attack animal",              default=True)
    allowed_costume  = models.BooleanField("allow costume",                    default=True)
    points_melee     = models.PositiveSmallIntegerField("melee points",        default=10)
    points_thrown    = models.PositiveSmallIntegerField("thrown points",       default=5)
    points_ranged    = models.PositiveSmallIntegerField("ranged points",       default=5)
    points_animal    = models.PositiveSmallIntegerField("animal points",       default=10)
    points_costume   = models.PositiveSmallIntegerField("costume points",      default=10)

    # Context Scoring Rules
    allowed_normal   = models.BooleanField("allow normal",                     default=True)
    allowed_raid     = models.BooleanField("allow raids",                      default=True)
    allowed_duel     = models.BooleanField("allow duels",                      default=True)
    points_normal    = models.PositiveSmallIntegerField("normal bonus points", default=0)
    points_raid      = models.PositiveSmallIntegerField("raid bonus points",   default=0)
    points_duel      = models.PositiveSmallIntegerField("duel bonus points",   default=0)

    # Indirect Rules
    allowed_indirect = models.BooleanField("allow indirect",                   default=True)
    points_indirect  = models.PositiveSmallIntegerField("indirect points",     default=10)

    # Respawn Rules
    respawn_count    = models.PositiveSmallIntegerField("respawn count",       default=32767)
    respawn_time     = models.DurationField("respawn time",                    default=timedelta(hours=6))

    respawn_start    = models.BooleanField("global respawn on start",          default=True)
    respawn_end      = models.BooleanField("global respawn on end",            default=True)
    respawn_delay    = models.DurationField("end respawn delay",               default=timedelta(minutes=30))

    # Flag Rules
    protect_flags    = models.BooleanField("prevent flag transfers",           default=False)

    # Functions
    def __str__(self):
        return str(self.config_name)

    def _isWeaponAllowed(self, report):
        '''Does this config allow this weapon'''
        if   report.weapon == MELEE:
            return self.allowed_melee
        elif report.weapon == THROWN:
            return self.allowed_thrown
        elif report.weapon == RANGED:
            return self.allowed_ranged
        elif report.weapon == ANIMAL:
            return self.allowed_animal
        elif report.weapon == COSTUME:
            return self.allowed_costume

    def _getWeaponScore(self, report):
        '''How many points does this config award this weapon'''
        if   report.weapon == MELEE:
            return self.points_melee
        elif report.weapon == THROWN:
            return self.points_thrown
        elif report.weapon == RANGED:
            return self.points_ranged
        elif report.weapon == ANIMAL:
            return self.points_animal
        elif report.weapon == COSTUME:
            return self.points_costume

    def _isContextAllowed(self, report):
        '''Does this config allow this context'''
        if   report.context == NORMAL:
            return self.allowed_normal
        elif report.context == RAID:
            return self.allowed_raid
        elif report.context == DUEL:
            return self.allowed_duel

    def _getContextScore(self, report):
        '''How many bonus points does this config award this context'''
        if   report.context == NORMAL:
            return self.points_normal
        elif report.context == RAID:
            return self.points_raid
        elif report.context == DUEL:
            return self.points_duel

    def isKillAllowed(self, report):
        '''Does this config allow this kill'''
        return self._isWeaponAllowed(report) and self._isContextAllowed(report)

    def getKillScore(self, report):
        '''How many points does this config award this kill'''
        return self._getWeaponScore(report) + self._getContextScore(report)

####################################################################################################

class EventScript(models.Model):
    '''ConfigScript with offset timing for an event in a game.'''

    # Config
    event_config   = models.ForeignKey(ConfigScript,            on_delete=models.CASCADE)
    
    # Timing
    event_start    = models.DurationField("event start offset", default=timedelta(days=0))
    event_duration = models.DurationField("event duration",     default=timedelta(hours=1))

    # Functions
    def __str__(self):
        return str(self.event_config)

    def isDuringEvent(self, game_time):
        return self.event_start < game_time and game_time < self.event_start + self.event_duration

####################################################################################################

class GameScript(models.Model):
    '''A primary ConfigScript and a selection of EventScripts.'''

    # Script Listings
    primary_script = models.ForeignKey(ConfigScript, on_delete=models.CASCADE)
    event_scripts  = models.ManyToManyField(EventScript)

    # Functions
    def __str__(self):
        return str(self.primary_script)

    def isDuringEvent(self, game_time) -> bool:
        for script in self.event_scripts:
            if script.isDuringEvent(game_time):
                return True
        return False

    def getConfig(self, game_time) -> ConfigScript:
        for script in self.event_scripts:
            if script.isDuringEvent(game_time):
                return script.event_config
        return self.primary_script

####################################################################################################

class Game(models.Model):
    '''Information about a game, a script, and timing.'''

    # Game Information
    title         = models.CharField("game title",        max_length=100)
    description   = models.TextField("game description")

    # Game Script
    game_script   = models.ForeignKey(GameScript,         on_delete=models.SET_NULL, null=True)

    # Game Timing
    game_start    = models.DateTimeField("game start")
    game_duration = models.DurationField("game duration", default=timedelta(weeks=1))

    # Functions
    def __str__(self):
        return str(self.title)

    def isDuringGame(self, time) -> bool:
        '''Is this game active at the given time?'''
        return self.game_start < time and time < self.game_start + self.game_duration

    def isDuringEvent(self, time) -> bool:
        '''Is the game currently in an event?'''
        return self.game_script.isDuringEvent(time - self.game_start)

    def getConfig(self, time) -> ConfigScript:
        '''Which configuration is active at a given time'''
        return self.game_script.getConfig(time - self.game_start)
        
####################################################################################################

class Flag(models.Model):
    '''Represents teams, status effects, etc.'''

    # General Configuration
    name                = models.CharField("flag name",                   max_length=100)
    visibility          = models.CharField("flag visibility",             max_length=3, choices=FLAG_VISIBILITY, default=EVERYONE)
    friendly            = models.BooleanField("flag friendly",            default=False)

    # Weapon Specific Permissions, Multipliers, and Bonuses
    allowed_melee       = models.BooleanField("melee kills allowed",      default=True)
    allowed_thrown      = models.BooleanField("thrown kills allowed",     default=True)
    allowed_ranged      = models.BooleanField("ranged kills allowed",     default=True)
    allowed_animal      = models.BooleanField("animal kills allowed",     default=True)
    allowed_costume     = models.BooleanField("costume kills allowed",    default=True)
    multiplier_melee    = models.FloatField("melee kill multiplier",      default=1)
    multiplier_thrown   = models.FloatField("thrown kill multiplier",     default=1)
    multiplier_ranged   = models.FloatField("ranged kill multiplier",     default=1)
    multiplier_animal   = models.FloatField("animal kill multiplier",     default=1)
    multiplier_costume  = models.FloatField("costume kill multiplier",    default=1)
    bonus_melee         = models.FloatField("melee kill bonus",           default=0)
    bonus_thrown        = models.FloatField("thrown kill bonus",          default=0)
    bonus_ranged        = models.FloatField("ranged kill bonus",          default=0)
    bonus_animal        = models.FloatField("animal kill bonus",          default=0)
    bonus_costume       = models.FloatField("costume kill bonus",         default=0)

    # Context Specific Permissions, Multipliers, and Bonuses
    allowed_normal      = models.BooleanField("melee kills allowed",      default=True)
    allowed_raid        = models.BooleanField("thrown kills allowed",     default=True)
    allowed_duel        = models.BooleanField("ranged kills allowed",     default=True)
    multiplier_normal   = models.FloatField("normal kill multiplier",     default=1)
    multiplier_raid     = models.FloatField("raid kill multiplier",       default=1)
    multiplier_duel     = models.FloatField("duel kill multiplier",       default=1)
    bonus_raid          = models.FloatField("raid kill bonus",            default=0)
    bonus_normal        = models.FloatField("normal kill bonus",          default=0)
    bonus_duel          = models.FloatField("duel kill bonus",            default=0)

    # Indirect Specific Permission, Multiplier, and Bonuse
    allowed_indirect    = models.BooleanField("indirect kills allowed",   default=True)
    multiplier_indirect = models.FloatField("indirect kill multiplier",   default=1)
    bonus_indirect      = models.FloatField("indirect kill bonus",        default=0)

    # Flag Transfer Behaviours
    on_kill             = models.CharField("flag action on kill",         max_length=3, choices=FLAG_TRANSFER, default=KEEP)
    on_death            = models.CharField("flag action on death",        max_length=3, choices=FLAG_TRANSFER, default=KEEP)

    # Functions
    def __str__(self):
        return str(self.name)

    def _isWeaponAllowed(self, report):
        '''Does this flag allow this weapon'''
        if   report.weapon == MELEE:
            return self.allowed_melee
        elif report.weapon == THROWN:
            return self.allowed_thrown
        elif report.weapon == RANGED:
            return self.allowed_ranged
        elif report.weapon == ANIMAL:
            return self.allowed_animal
        elif report.weapon == COSTUME:
            return self.allowed_costume

    def _getWeaponMultiplier(self, report):
        '''How much does this flag multiply points for this weapon by'''
        if   report.weapon == MELEE:
            return self.multiplier_melee
        elif report.weapon == THROWN:
            return self.multiplier_thrown
        elif report.weapon == RANGED:
            return self.multiplier_ranged
        elif report.weapon == ANIMAL:
            return self.multiplier_animal
        elif report.weapon == COSTUME:
            return self.multiplier_costume

    def _getWeaponBonus(self, report):
        '''How many bonus points does this flag award this weapon'''
        if   report.weapon == MELEE:
            return self.bonus_melee
        elif report.weapon == THROWN:
            return self.bonus_thrown
        elif report.weapon == RANGED:
            return self.bonus_ranged
        elif report.weapon == ANIMAL:
            return self.bonus_animal
        elif report.weapon == COSTUME:
            return self.bonus_costume

    def _isContextAllowed(self, report):
        '''Does this flag allow this context'''
        if   report.context == NORMAL:
            return self.allowed_normal
        elif report.context == RAID:
            return self.allowed_raid
        elif report.context == DUEL:
            return self.allowed_duel

    def _getContextMultiplier(self, report):
        '''How much does this flag multiply points for this context by'''
        if   report.context == NORMAL:
            return self.multiplier_normal
        elif report.context == RAID:
            return self.multiplier_raid
        elif report.context == DUEL:
            return self.multiplier_duel

    def _getContextBonus(self, report):
        '''How many bonus points does this flag award this context'''
        if   report.context == NORMAL:
            return self.bonus_normal
        elif report.context == RAID:
            return self.bonus_raid
        elif report.context == DUEL:
            return self.bonus_duel

    def isKillAllowed(self, report):
        '''Does this flag allow this kill'''
        return self._isWeaponAllowed(report) and self._isContextAllowed(report)

    def getKillMultiplier(self, report):
        '''How much does this flag multiply points for this kill by'''
        return self._getWeaponMultiplier(report) * self._getContextMultiplier(report)

    def getKillBonus(self, report):
        '''How many bonus points does this flag award this kill'''
        return self._getWeaponBonus(report) + self._getContextBonus(report)

####################################################################################################

class Player(models.Model):
    '''Connects an Assassin to a Game and holds in-game data about them.'''
    # Link Fields
    assassin       = models.ForeignKey(Assassin,  on_delete=models.SET_NULL, null=True)
    game           = models.ForeignKey(Game,      on_delete=models.SET_NULL, null=True)

    # In-Game Data
    alive          = models.BooleanField("is player alive", default=False)
    game_respawns  = models.PositiveSmallIntegerField("game respawns")
    event_respawns = models.PositiveSmallIntegerField("event respawns")
    next_respawn   = models.DateTimeField("next respawn")
    flags          = models.ManyToManyField(Flag, verbose_name="player flags")
    
    # Functions
    def __str__(self):
        return str(self.assassin)

    def tryRespawn(self, time) -> bool:
        if self.alive:
            return False # Respawn failed: Already alive.

        if not self.game.isDuringGame(time):
            return False # Respawn failed: Invalid time.

        if time < self.next_respawn:
            return False # Respawn failed: Not ready to respawn yet.

        if self.game.isDuringEvent(time):
            if self.event_respawns > 0:
                self.alive = True
                self.event_respawns -= 1
                self.next_respawn = datetime(year=16777216)
                self.save()
                return True # Respawned in event
        elif self.game_respawns > 0:
            self.alive = True
            self.game_respawns -= 1
            self.next_respawn = datetime(year=16777216)
            self.save()
            return True # Respawned in game

####################################################################################################

class DirectReport(models.Model):
    '''A report of a kill or death.'''

    # Players
    killer           = models.ForeignKey(Player,               on_delete=models.SET_NULL, null=True, related_name="kills")
    victim           = models.ForeignKey(Player,               on_delete=models.SET_NULL, null=True, related_name="deaths")
    
    # Information
    weapon           = models.CharField("kill weapon",         max_length=3, choices=KILL_METHODS, default=MELEE)
    context          = models.CharField("kill context",        max_length=3, choices=KILL_CONTEXTS, default=NORMAL)
    location         = models.CharField("kill location",       max_length=256)
    date             = models.DateTimeField("kill date",       auto_now=True)

    # Report Content
    killer_report    = models.TextField("killer report", null=True, blank=True)
    victim_report    = models.TextField("victim report", null=True, blank=True)
    # killer_media     = models.FileField("killer report media", null=True, blank=True)
    # victim_media     = models.FileField("killer report media", null=True, blank=True)

    # Validation
    killer_validated = models.BooleanField("killer validated", default=False)
    victim_validated = models.BooleanField("victim validated", default=False)

    # Functions
    def __str__(self):
        return str(self.killer) + " --" + str(self.weapon.label) + "-> " + str(self.victim)

    def _isValid(self, game) -> bool:
        '''Does the kill occur between valid players at a valid time for a given game?'''
        v_killer = self.killer.game == game
        v_victim = self.victim.game == game
        v_date   = game.isDuringGame(self.date)
        return v_killer and v_victim and v_date

    def _isAllowed(self) -> bool:
        '''Does the script and flags agree to the weapon and context?'''
        for flag in self.killer.flags:
            if not flag.isKillAllowed(self):
                return False # Flag disallows this kill
            if flag.friendly and flag in self.victim.flags:
                return False # Killer and victim share a friendly flag
        return self.killer.game.getConfig(self.date).isKillAllowed(self)

    def _isAgreed(self) -> bool:
        '''Do both players agree to the kill?'''
        return self.killer_validated and self.victim_validated

    def didKill(self, game) -> bool:
        '''Does the report constitute a kill?'''
        return self._isValid(game) and self._isAllowed(game)

    def getPoints(self, game) -> int:
        '''How many points to give the killer?'''
        if not self.didKill() or not self._isAgreed():
            return 0

        points     = game.getConfig(self.date).getKillScore(self)
        multiplier = 1
        bonus      = 0
        for flag in self.killer.flags:
            multiplier *= flag.getKillMultiplier(self)
            bonus      += flag.getKillBonus(self)
        return points * multiplier + bonus

####################################################################################################

class IndirectReport(models.Model):
    '''A report of a trap being laid or sprung.'''

    # Players
    trapper         = models.ForeignKey(Player,               on_delete=models.SET_NULL, null=True, related_name="traps_set")
    target          = models.ForeignKey(Player,               on_delete=models.SET_NULL, null=True, related_name="traps_recieved")
    
    # Information
    location        = models.CharField("trap location",       max_length=256)
    date_set        = models.DateTimeField("trap laid",       auto_now=True)
    date_sprung     = models.DateTimeField("trap sprung",     null=True, blank=True)

    # Report Content
    trapper_report  = models.TextField("trapper report",      null=True, blank=True)
    target_report   = models.TextField("target report",       null=True, blank=True)
    # trapper_media   = models.FileField("trapper report media",null=True, blank=True)
    # target_media    = models.FileField("target report media", null=True, blank=True)

    # Validation
    trap_sprung     = models.BooleanField("trap successful",  default=False)
    trap_successful = models.BooleanField("trap successful",  default=False)

    # Functions
    def __str__(self):
        return str(self.killer) + " --Indirect-> " + str(self.victim)

    def _isValid(self, game) -> bool:
        '''Does the trap occur between valid players at a valid time for a given game?'''
        v_trapper     = self.trapper.game == game
        v_target      = self.target.game == game
        v_date_set    = game.isDuringGame(self.date_set)
        v_date_sprung = game.isDuringGame(self.date_sprung)
        return v_trapper and v_target and v_date_set and v_date_sprung

    def _isAllowed(self, game) -> bool:
        '''Does the script agree to the trap?'''
        for flag in self.trapper.flags:
            if not flag.allowed_indirect:
                return False # Flag disallows this kill
            if flag.friendly and flag in self.target.flags:
                return False # Killer and victim share a friendly flag
        return game.getConfig(self.date_set).allowed_indirect

    def _isAgreed(self) -> bool:
        '''Did the trap spring and successfully kill?'''
        return self.trap_sprung and self.trap_successful

    def didKill(self, game) -> bool:
        '''Does the report constitute a kill?'''
        return self._isValid(game) and self._isAllowed(game) and self._isAgreed()

    def getPoints(self, game) -> int:
        '''How many points to give the killer?'''
        if not self.didKill():
            return 0

        points     = game.getConfig(self.date).points_indirect
        multiplier = 1
        bonus      = 0
        for flag in self.killer.flags:
            multiplier *= flag.multiplier_indirect
            bonus      += flag.bonus_indirect
        return points * multiplier + bonus

####################################################################################################

class GeneralReport(models.Model):
    '''A non-kill/death/indirect report.'''
    # Player
    player      = models.ForeignKey(Player,         on_delete=models.SET_NULL, null=True)

    # Information
    location    = models.CharField("kill location", max_length=256)
    date        = models.DateTimeField("kill date", auto_now=True)

    # Report Content
    report_text = models.TextField("killer report")
    # report_media = models.FileField("killer report media")

    # Functions
    def __str__(self):
        return str(self.player) + "_" + str(self.date)

