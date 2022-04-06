from django.urls import path
from . import views

# Account URLs:
#   account
#   login
#   logout
#   register
#   profile

urlpatterns = [
    # Account Settings Page
    path('', views.account, name="account"),

    # Login
    path('login/', views.login, name="login"),
    # Logout
    path('logout/', views.logout, name="logout"),
    # Register
    path('register/', views.register, name="register"),

    # Profile
    path('profile/<str:pk>/', views.profile, name="profile"),
]