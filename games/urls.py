from django.urls import path
from . import views

# Games URLs:
#   game_list
#   game

urlpatterns = [
    # Game List Page and Game Page
    path('', views.gameList, name="game_list"),
    path('<str:pk>/', views.game, name="game"),
]