from django.urls import path
from . import views

# Base URLs:
#   home
#   about
#   blog
#   blog_post
#   cabal
#   discord

urlpatterns = [
    # Home page
    path('', views.home, name="home"),

    # About the Guild Page
    path('about/', views.about, name="about"),

    # Blog Page and Article Page
    path('blog/', views.blog, name="blog"),
    path('blog/<str:pk>/', views.blogPost, name="blog_post"),

    # Cabal Page
    path('cabal/', views.cabal, name="cabal"),

    # Discord Page
    path('discord/', views.discord, name="discord"),
]