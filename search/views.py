from django.shortcuts import redirect, render
from django.db.models import Q, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from index.models import *

# Create your views here.


def search_view(request, page):
    if request.method == "GET":
        kword = request.session.get("kword", "")
        if kword:
            songs = (
                Song.objects.filter(
                    Q(name__icontains=kword) | Q(singer__icontains=kword)
                )
                .order_by("-name")
                .all()
            )
        else:
            songs = Song.objects.order_by("-name").all()[:50]
        paginator = Paginator(songs, 8)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        # 添加歌曲的搜索次数
        if kword:
            song_list = Song.objects.filter(name__icontains=kword)
            for s in song_list:
                dynamic = Dynamic.objects.filter(song_id=s.id)
                if dynamic:
                    dynamic.update(search=F("search") + 1)
                else:
                    dynamic = Dynamic(plays=0, search=1, download=0, song=s)
                    dynamic.save()
        return render(request, "search.html", locals())

    else:
        request.session["kword"] = request.POST.get("kword", "")
        return redirect(reverse("search:search", kwargs={"page": 1}))