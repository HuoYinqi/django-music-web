from django.urls import path
from .views import *

app_name = "play"

urlpatterns = [
    path("<int:id>.html", play, name="play"),
    path("download/<int:id>", download_view, name="download"),
]
