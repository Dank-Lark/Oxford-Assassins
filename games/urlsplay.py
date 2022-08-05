from django.urls import path
from . import views

# Games URLs:
#   Games
#   Game by ID

urlpatterns = [
    # Play
    path('', views.play, name="play"),
]