from django.core.cache import cache

from celery_task.celery import app

from django.conf import settings
from home import models
from serializers import home


@app.task
def update_banner_list():
    queryset = models.Banner.objects.filter(is_delete=False, is_show=True).order_by('-orders')[
               :settings.HOME_BANNER_COUNT]
    banner_list = home.BannerModelSerializer(instance=queryset, many=True).data
    for banner in banner_list:
        banner['image'] = '%s%s' % (settings.BACKEND_URL, banner['image'])
    cache.set(settings.HOME_BANNER_LIST, banner_list, settings.HOME_BANNER_EXPIRATION)
    return banner_list
