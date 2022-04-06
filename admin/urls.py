from django.urls import path
from . import views

# Admin URLs:
#   admin_home
#   admin_about
#   admin_blog
#   admin_cabal
#   admin_users
#   admin_games

urlpatterns = [
    # Admin Home Page
    path('', views.home, name="admin_home"),

    # About the Guild Admin Page
    path('about/', views.about, name="admin_about"),

    # Blog Admin Page
    path('blog/', views.blog, name="admin_blog"),

    # Cabal Admin Page
    path('cabal/', views.cabal, name="admin_cabal"),

    # Users Admin Page
    path('users/', views.users, name="admin_users"),

    # Games Admin Page
    path('games/', views.games, name="admin_games"),
]