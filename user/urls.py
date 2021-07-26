from django.urls import path
from .views import *


app_name = "user"

urlpatterns = [
    path("login/", user_login, name="login"),
    path("register", user_register, name="register"),
    path("logout", user_logout, name="logout"),
    path("detail/", user_detail, name="user_detail"),
]
