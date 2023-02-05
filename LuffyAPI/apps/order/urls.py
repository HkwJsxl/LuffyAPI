from django.urls import path, re_path

from views import order

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('pay', order.OrderPayView)
# router.register('pay/success', order.OrderPayView)

"""
1）支付接口(需要登录认证)：前台提交商品等信息，得到支付链接
    post方法
分析：支付宝回调
    同步：get给前台 => 前台可以在收到支付宝同步get回调时，ajax异步在给消息同步给后台，也采用get，后台处理前台的get请求
    异步：post给后台 => 后台直接处理支付宝的post请求
2）支付回调接口(不需要登录认证：哪个订单(订单信息中有非对称加密)、支付宝压根不可能有你的token)：
    get方法：处理前台来的同步回调（不一定能收得到，所有不能在该方法完成后台订单状态等信息操作）
    post方法：处理支付宝来的异步回调
3）订单状态确认接口：随你前台任何时候来校验订单状态的接口
"""

urlpatterns = [

]

urlpatterns += router.urls
