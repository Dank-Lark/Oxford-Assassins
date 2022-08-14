from django.contrib import admin
from games.models import *

class XASGroupAdmin(admin.ModelAdmin):
    list_display = ("umpire", "reference", "created")
admin.site.register(XASGroup, XASGroupAdmin)

class FlagAdmin(admin.ModelAdmin):
    list_display = ("xas_group", "name", "visibility", "friendly", "on_kill", "on_death")
admin.site.register(Flag, FlagAdmin)

class InfoLoreAdmin(admin.ModelAdmin):
    list_display = ("xas_group", "title", "release_start", "release_end", "public")
admin.site.register(InfoLore, InfoLoreAdmin)

class ConfigScriptAdmin(admin.ModelAdmin):
    list_display = ("xas_group", "config_name", "respawn_count", "respawn_time", "respawn_start", "respawn_end", "respawn_delay", "protect_flags")
admin.site.register(ConfigScript, ConfigScriptAdmin)

class EventScriptAdmin(admin.ModelAdmin):
    list_display = ("xas_group", "event_config", "event_start", "event_duration")
admin.site.register(EventScript, EventScriptAdmin)

class GameScriptAdmin(admin.ModelAdmin):
    list_display = ("xas_group", "primary_script", "report_deadline", "report_bounty")
admin.site.register(GameScript, GameScriptAdmin)

class GameAdmin(admin.ModelAdmin):
    list_display = ("xas_group", "title", "game_script", "game_start", "game_duration")
admin.site.register(Game, GameAdmin)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ("assassin", "game", "alive", "game_respawns", "event_respawns", "next_respawn")
admin.site.register(Player, PlayerAdmin)

class DirectReportAdmin(admin.ModelAdmin):
    list_display = ("killer", "victim", "weapon", "context", "location", "kill_date", "killer_validated", "victim_validated", "confirm_date")
admin.site.register(DirectReport, DirectReportAdmin)

class IndirectReportAdmin(admin.ModelAdmin):
    list_display = ("trapper", "target", "location", "date_set", "date_sprung", "trap_sprung", "trap_successful")
admin.site.register(IndirectReport, IndirectReportAdmin)

class GeneralReportAdmin(admin.ModelAdmin):
    list_display = ("player", "location", "date")
admin.site.register(GeneralReport, GeneralReportAdmin)

class PlayerBonusAdmin(admin.ModelAdmin):
    list_display = ("player", "date", "points")
admin.site.register(PlayerBonus, PlayerBonusAdmin)

class FlagBonusAdmin(admin.ModelAdmin):
    list_display = ("flag", "date", "points")
admin.site.register(FlagBonus, FlagBonusAdmin)

class PlayerBountyAdmin(admin.ModelAdmin):
    list_display = ("player", "points", "date_set", "claimed_by", "date_claimed")
admin.site.register(PlayerBounty, PlayerBountyAdmin)