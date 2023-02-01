from django.core.cache import cache

from rest_framework.viewsets import GenericViewSet

from . import models
from .serializers import BannerModelSerializer
from LuffyAPI.extension.mixins import ReListModelMixin
from LuffyAPI.settings import dev
from LuffyAPI.extension.response import APIResponse


class BannerView(ReListModelMixin, GenericViewSet):
    queryset = models.Banner.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = BannerModelSerializer

    def list(self, request, *args, **kwargs):
        banner_list = cache.get(dev.HOME_BANNER_LIST)
        if banner_list:
            return APIResponse(data=banner_list)
        response = super().list(request, *args, **kwargs)
        cache.set(dev.HOME_BANNER_LIST, response.data.get('data'), dev.HOME_BANNER_EXPIRATION)
        return response
