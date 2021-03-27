from django.core import paginator
from django.http.response import Http404
from index.models import *
import time

from django.shortcuts import redirect, render, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def comment_view(request, id):
    if request.method == "POST":
        text = request.POST.get("content", "")
        if request.user.username:
            user = request.user.username
        else:
            user = "匿名用户"
        if text:
            comment = Comment()
            comment.user = user
            comment.text = text
            comment.date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
            comment.song_id = id
            comment.save()
        return redirect(reverse("comment:comment", kwargs={"id": id}))
    else:
        song = Song.objects.get(id=id)
        if not song:
            raise Http404
        c = Comment.objects.filter(song_id=id).order_by("date")
        paginator = Paginator(c, 10)
        page_id = request.GET.get("page", 1)
        try:
            page = paginator.page(page_id)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        return render(request, "comment.html", locals())