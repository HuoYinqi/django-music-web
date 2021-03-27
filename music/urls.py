"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("index.urls", namespace="index")),
    path("play/", include("play.urls", namespace="play")),
    path("ranking/", include("ranking.urls", namespace="ranking")),
    path("search/", include("search.urls", namespace="search")),
    path("comment/", include("comment.urls", namespace="comment")),
    # 配置媒体资源的路由信息
    re_path(
        "media/(?P<path>.*)",
        serve,
        {"document_root": settings.MEDIA_ROOT},
        name="media",
    ),
    # 定义静态资源的路由信息
    re_path(
        "static/(?P<path>.*)",
        serve,
        {"document_root": settings.STATIC_ROOT},
        name="static",
    ),
]
