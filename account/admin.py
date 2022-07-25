from django.contrib import admin
from .models import User, Assassin

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "request_pay", "paid", "assassin")
admin.site.register(User, UserAdmin)

class AssassinAdmin(admin.ModelAdmin):
    list_display = ("pseudonym", "discordName", "discordTag", "subject", "college", "startYear", "address", "room")
admin.site.register(Assassin, AssassinAdmin)