from rest_framework.viewsets import GenericViewSet

from order import models
from serializers import order
from LuffyAPI.extension.mixins import ReCreateModelMixin
from LuffyAPI.extension.response import APIResponse
from LuffyAPI.extension.auth import TokenHeaderAuthentication


class OrderPayView(GenericViewSet, ReCreateModelMixin):
    authentication_classes = (TokenHeaderAuthentication,)

    queryset = models.Order.objects.all()
    serializer_class = order.OrderPayModelSerializer

    def perform_create(self, serializer):
        serializer.save()
        return APIResponse(data=serializer.context.get('pay_url'))
