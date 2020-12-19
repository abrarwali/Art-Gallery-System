from django.urls import path,re_path
from Users.views import UserRegistrationView,UserLogoutView,UserLoginView
from django.contrib import auth

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='User-Registration'),
    path('login/', UserLoginView.as_view(), name='User-Login'),
    path('logout/', UserLogoutView.as_view(), name='User-Logout'),

]