from django.db import models
from user.models import UserInfo
from course.models import Course


class OrderBaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    class Meta:
        abstract = True


class Order(OrderBaseModel):
    """订单模型"""
    status_choices = (
        (0, '待支付'),
        (1, '已支付'),
        (2, '已取消'),
        (3, '超时取消'),
    )
    pay_choices = (
        (1, '支付宝'),
        (2, '微信支付'),
    )
    subject = models.CharField(max_length=150, verbose_name="订单标题")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="订单总价", default=0)
    # 自己生成
    out_trade_no = models.CharField(max_length=64, verbose_name="订单号", unique=True)
    # 支付宝返回的
    trade_no = models.CharField(max_length=64, null=True, verbose_name="流水号")

    order_status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="订单状态")
    pay_type = models.SmallIntegerField(choices=pay_choices, default=1, verbose_name="支付方式")

    pay_time = models.DateTimeField(null=True, verbose_name="支付时间")

    user = models.ForeignKey(UserInfo, related_name='order_user', on_delete=models.DO_NOTHING, db_constraint=False,
                             verbose_name="下单用户")

    class Meta:
        db_table = "luffy_order"
        verbose_name = "订单记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s - ￥%s" % (self.subject, self.total_amount)

    @property
    def courses(self):
        data_list = []
        for item in self.order_courses.all():
            data_list.append({
                "id": item.id,
                "course_name": item.course.name,
                "real_price": item.real_price,
            })
        return data_list


class OrderDetail(OrderBaseModel):
    """订单详情"""
    order = models.ForeignKey(Order, related_name='order_courses', on_delete=models.CASCADE, db_constraint=False,
                              verbose_name="订单")
    course = models.ForeignKey(Course, related_name='course_orders', on_delete=models.SET_NULL, db_constraint=False,
                               verbose_name="课程", null=True)

    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="课程原价", default=0)
    real_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="课程实价", default=0)

    class Meta:
        db_table = "luffy_order_detail"
        verbose_name = "订单详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        try:
            return "%s的订单：%s" % (self.course.name, self.order.out_trade_no)
        except Exception:
            return super().__str__()
