from django.urls import path
from . import views

# Base URLs:
#   base

urlpatterns = [
    # One page
    path('', views.home, name="home"),
]