from django.http.response import StreamingHttpResponse
from django.shortcuts import render
from urllib.request import unquote

from index.models import *

# Create your views here.


def play(request, id):
    song = Song.objects.get(id=id)
    play_list = request.session.get("play_list", [])
    exist = False
    if play_list:
        for i in play_list:
            if int(id) == i["id"]:
                exist = True
                break
    if exist == False:
        play_list.append(
            {
                "id": int(id),
                "singer": song.singer,
                "name": song.name,
                "time": song.time,
                "url": song.file.url,
            }
        )
    play_urls = []
    for info in play_list:
        song_id = info["id"]
        temp = Song.objects.get(id=song_id)
        play_urls.append(temp.file.url)
    request.session["play_list"] = play_list
    if song.lyrics != "":
        path = unquote(song.lyrics.url)[1::]
        with open(path, "r", encoding="UTF-8") as f:
            lyrics = f.read()
    else:
        lyrics = "暂无歌词"
    d = Dynamic.objects.filter(song_id=int(id)).first()
    plays = d.plays + 1 if d else 1
    Dynamic.objects.update_or_create(song_id=id, defaults={"plays": plays})

    return render(request, "play.html", locals())


def download_view(request, id):
    dynamic = Dynamic.objects.filter(song_id=id).first()
    download = dynamic.download + 1 if dynamic else 1
    Dynamic.objects.update_or_create(song_id=id, defaults={"download": download})

    song = Song.objects.get(id=id)
    file = unquote(song.file.url)[1::]

    def file_iterator(file, chunk_size=512):
        with open(file, "rb") as f:
            while True:
                content = f.read(chunk_size)
                if content:
                    yield content
                else:
                    break

    name = song.name + ".m4a"
    response = StreamingHttpResponse(file_iterator(file))
    response["Content-Type"] = "application/octet-stream"
    response["Content-Disposition"] = "arrachment;filename=%s" % (name)
    return response
