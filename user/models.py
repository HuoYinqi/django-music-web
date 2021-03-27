from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    qq = models.CharField("QQ号码", max_length=20)

    def __str__(self) -> str:
        return self.username