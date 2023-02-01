import os

from django.db import models
from django.contrib.auth.models import AbstractUser


def user_directory_path(instance, filename):
    return os.path.join('user_dir_path', instance.name, "avatars", filename)


class UserInfo(AbstractUser):
    mobile = models.CharField(verbose_name='手机号', max_length=11, unique=True)
    avatar = models.ImageField(verbose_name='头像', upload_to=user_directory_path, default='avatars/default.png')

    class Meta:
        db_table = 'luffy_userinfo'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
