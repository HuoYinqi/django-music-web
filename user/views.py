from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.contrib.auth import authenticate, login, logout

from user.models import MyUser

# Create your views here.


def user_login(request):
    page_title = "用户登录"
    is_confirm_password = False
    button = "登录"
    url_text = "用户注册"
    url_name = "user:register"
    if request.method == "POST":
        u = request.POST.get("username", "")
        p = request.POST.get("password", "")
        if MyUser.objects.filter(username=u):
            user = authenticate(username=u, password=p)
            if user:
                if user.is_active:
                    login(request, user)
                return redirect(reverse("index:index"))
            else:
                tips = "账号密码错误，请重新输入"
        else:
            tips = "用户不存在，请注册"
            return render(request, "login.html", locals())
    else:
        if request.user.username:
            return redirect(reverse("index:index"))
        else:
            return render(request, "login.html", locals())


def user_register(request):
    page_title = "用户注册"
    is_confirm_password = True
    button = "注册"
    url_text = "用户登录"
    url_name = "user:login"
    if request.method == "POST":
        u = request.POST.get("username", "")
        p = request.POST.get("password", "")
        p1 = request.POST.get("password1", "")
        if MyUser.objects.filter(username=u):
            tips = "该用户以存在"
            return render(request, "login.html", locals())

        elif len(p1) < 6:
            tips = "密码长度至少大于六位"

        elif p1 != p:
            tips = "两次密码输入不一致"

        else:
            d = {"username": u, "password": p, "is_active": 1}
            user = MyUser.objects.create_user(**d)
            user.save()
            tips = "注册成功请登录"
            logout(request)
            return redirect(reverse("user:login"))

    return render(request, "login.html", locals())


def user_logout(request):
    if request.user.username:
        logout(request)
    return redirect(reverse("index:index"))


def user_detail(request):
    if not request.user.username:
        return redirect(reverse("user:login"))
    return render(request, "user_detail.html", locals())