import uuid

from django.db import transaction

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from order import models
from course.models import Course
from LuffyAPI.libs.pay_api import ali_pay


class OrderPayModelSerializer(serializers.ModelSerializer):
    # 要支持单购物和群购物(购物车)，前台要提交 课程主键(支持多个)
    courses = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True,
                                                 write_only=True)

    class Meta:
        model = models.Order
        fields = (
            'subject',
            'total_amount',
            'pay_type',
            'courses',
        )
        extra_kwargs = {
            'total_amount': {'required': True},
            'pay_type': {'required': True},
        }

    """
        # 1）订单总价校验
        # 2）生成订单号
        # 3）支付用户：request.user
        # 4）支付链接生成
        # 5）入库(两个表)的信息准备
    """

    def _check_total_amount(self, attrs):
        # 不考虑打折
        total_amount = self.initial_data.get('total_amount')
        # initial_data是最原始的数据，拿不到serializers.PrimaryKeyRelatedField之后的内容
        # 错误：course_list = self.initial_data.get('courses')
        course_list = attrs.get('courses')
        price_total = 0
        for course in course_list:
            price_total += course.price
        if float(total_amount) != float(price_total):
            raise ValidationError('订单总价错误.')
        return total_amount

    @staticmethod
    def _generate_out_trade_no():
        out_trade_no = uuid.uuid4()
        return str(out_trade_no).replace('-', '')

    def _get_user(self):
        return self.context.get('request').user

    def _generate_pay_url(self, out_trade_no, total_amount):
        subject = self.initial_data.get('subject')
        pay_url = ali_pay.pay(out_trade_no, subject, total_amount)
        return pay_url

    @staticmethod
    def _insert_fields(attrs, user, out_trade_no):
        attrs['user'] = user
        attrs['out_trade_no'] = out_trade_no

    def validate(self, attrs):
        # 判断前端传过来的总价是否正确
        total_amount = self._check_total_amount(attrs)
        # 生成订单号
        out_trade_no = self._generate_out_trade_no()
        # 返回支付用户
        user = self._get_user()
        # 生成支付链接
        pay_url = self._generate_pay_url(out_trade_no, total_amount)
        # views返回一个支付链接
        self.context['pay_url'] = pay_url
        # 入库
        self._insert_fields(attrs, user, out_trade_no)
        return attrs

    def create(self, validated_data):
        courses = validated_data.pop('courses')
        with transaction.atomic():
            order_obj = models.Order.objects.create(**validated_data)
            course_detail_list = []
            for course in courses:
                course_detail_list.append(
                    models.OrderDetail(
                        course=course, order=order_obj,
                        price=course.price,
                        real_price=course.price
                    )
                )
            models.OrderDetail.objects.bulk_create(course_detail_list)
        return validated_data
