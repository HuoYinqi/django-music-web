from django.urls import path
from .views import *

app_name = "ranking"

urlpatterns = [path("", ranking_view, name="ranking")]