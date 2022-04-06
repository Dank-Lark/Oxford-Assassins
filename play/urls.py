from django.urls import path
from . import views

urlpatterns = [
    # Play Overview Page
    path('', views.overview, name="play_overview"),

    # In-Game Events Page and Event Page
    path('events/', views.eventsList, name="play_events_list"),
    path('events/<str:pk>/', views.event, name="play_event"),

    # In-Game Map Page
    path('map/', views.map, name="play_map"),

    # In-Game Report Page
    path('report/', views.report, name="play_report"),

    # In-Game Stats Page
    path('stats/', views.stats, name="play_stats"),
    path('stats/<str:pk>/', views.userStats, name="play_user_stats"),

    # In-Game Teams Page
    path('teams/', views.teams, name="play_teams"),
]