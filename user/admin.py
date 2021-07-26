from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ["username", "qq"]
    search_fields = ["name"]
    fieldsets = list(UserAdmin.fieldsets)
    fieldsets[1] = (
        _("个人信息"),
        {"fields": ("first_name", "last_name", "email", "qq")},
    )
