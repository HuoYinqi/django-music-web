from django.urls import path

from .views import *

app_name = "comment"

urlpatterns = [path("<int:id>.html", comment_view, name="comment")]
