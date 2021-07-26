from django.apps import AppConfig
import os

default_app_config = "user.UserConfig"


def get_current_app_name(file_):
    return os.path.split(os.path.dirname(file_))[-1]


class UserConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = "用户列表"