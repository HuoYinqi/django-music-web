from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    song_dynamics = Dynamic.objects.select_related("song")
    popular = song_dynamics.order_by("-plays").all()[:10]
    searchs = song_dynamics.order_by("-search").all()[:4]
    downloads = song_dynamics.order_by("-download").all()[:7]
    labels = Label.objects.all()

    return render(request, "base.html", locals())
