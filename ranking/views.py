from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from index.models import *

# Create your views here.


def ranking_view(request):
    song_dynamics = Dynamic.objects.select_related("song")
    labels = Label.objects.all()
    t = request.GET.get("type", "")
    if t:
        song_dynamics = (
            Dynamic.objects.select_related("song")
            .filter(song__label=t)
            .order_by("-plays")
        ).all()[:10]
    else:
        song_dynamics = (
            Dynamic.objects.select_related("song").order_by("-plays")
        ).all()[:10]
    return render(request, "ranking.html", locals())
