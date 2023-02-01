from django.db import models

from LuffyAPI.extension.models import BaseModel


class Banner(BaseModel):
    name = models.CharField(verbose_name='图片名称', max_length=32, null=True, blank=True)
    image = models.ImageField(verbose_name='图片', upload_to='static/banner/')
    link = models.CharField(verbose_name='链接', max_length=64)
    introduction = models.TextField(verbose_name='详情介绍', null=True, blank=True)

    class Meta:
        db_table = 'luffy_banner'
        verbose_name = '轮播表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
