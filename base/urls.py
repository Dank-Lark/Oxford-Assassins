from django.urls import path
from . import views

# Base URLs:
#   home
#   about
#   cabal
#   discord

urlpatterns = [
    # Home page
    path('', views.home, name="home"),

    # About the Guild Page
    path('about/', views.about, name="about"),

    # Cabal Page
    path('cabal/', views.cabal, name="cabal"),

    # Discord Page
    path('discord/', views.discord, name="discord"),
]