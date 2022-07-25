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

    # Update User Form Submission
    path('update_user/', views.updateUser, name="updateUser"),
    # Change Password
    path('change_password/', views.changePassword, name="changePassword"),
    # Register Assassin Form Submission
    path('create_assassin/', views.createAssassin, name="createAssassin"),
    # Update Assassin Form Submission
    path('update_assassin/', views.updateAssassin, name="updateAssassin"),
    # Pay for Membership
    path('pay_membership/', views.payMembership, name="payMembership"),

    # Login
    path('login/', views.loginForm, name="login"),
    # Logout
    path('logout/', views.logoutForm, name="logout"),
    # Register
    path('register/', views.registerForm, name="register"),

    # Profile
    path('profile/<str:pk>/', views.profile, name="profile"),
]