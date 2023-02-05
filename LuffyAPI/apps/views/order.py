from rest_framework.viewsets import GenericViewSet

from LuffyAPI.extension.mixins import ReListModelMixin, ReRetrieveModelMixin
from order import models
from serializers import order


class OrderPayView(GenericViewSet, ReListModelMixin):
    queryset = models.Order.objects.filter()
    serializer_class = order.OrderPayModelSerializer
