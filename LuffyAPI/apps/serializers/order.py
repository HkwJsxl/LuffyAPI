from rest_framework import serializers

from order import models


class OrderPayModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = (
            'name',
        )
