from django.db import models


class BaseModel(models.Model):
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)
    is_show = models.BooleanField(verbose_name='是否显示', default=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    last_update_time = models.DateTimeField(verbose_name='最后修改时间', auto_now=True)
    orders = models.IntegerField(verbose_name='优先级')

    class Meta:
        abstract = True
