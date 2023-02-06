import datetime

from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from order import models
from serializers import order
from LuffyAPI.extension.mixins import ReCreateModelMixin
from LuffyAPI.extension.response import APIResponse
from LuffyAPI.extension.auth import TokenHeaderAuthentication
from LuffyAPI.libs.pay_api.client import alipay
from LuffyAPI.extension.logger import log


class OrderPayView(GenericViewSet, ReCreateModelMixin):
    authentication_classes = (TokenHeaderAuthentication,)

    queryset = models.Order.objects.all()
    serializer_class = order.OrderPayModelSerializer

    def perform_create(self, serializer):
        serializer.save()
        return APIResponse(data={'pay_url': serializer.context.get('pay_url')})


class OrderPaySuccessView(APIView):
    def get(self, request, *args, **kwargs):
        # 前台的get同步回调
        # print(request.query_params)
        """
        2023.02.06
        <QueryDict: {
            'charset': ['utf-8'],
            'out_trade_no': ['ab09f059fbb5443bb2648fcda0010071'],
            'method': ['alipay.trade.page.pay.return'],
            'total_amount': ['39.00'],
            'sign': ['nqy8hf/QZ+l+GbD71uceKxYFMMXPpJTlxKZRr+M/i/9OVQI8cwaP1ZY+0bqcEzuRvf/QtWDrDptaV1OczvMmZtm6WwT86VpSfS7bbta26YVefX6d2tCuJm51OD0lWa2/U/N2OBJiCfCXDGa+Uth4RH20jTKkyrX7tXdmQTQssDcZpRFENQ8hGqrNf6D3vSYKM9D08W8As+XLSfTmJkoKmBz3fHw1ivlLIcT6G4bbQN7ui4J/Xs/vfxqbrjNCgv1Xpn0+3LpUry3XWHP19+EM861fKMoY/+CBUif1IO1NDwxb1xnPDtSENr/yuVWusjQxwfznG5I6dZgH93WBhLKfVw=='],
            'trade_no': ['2023020622001435600502030659'],
            'auth_app_id': ['2021000122613847'],
            'version': ['1.0'],
            'app_id': ['2021000122613847'],
            'sign_type': ['RSA2'],
            'seller_id': ['2088621995167585'],
            'timestamp': ['2023-02-06 13:51:16']}>
        """

        out_trade_no = request.query_params.get('out_trade_no')
        order_obj = models.Order.objects.filter(out_trade_no=out_trade_no).first()
        if order_obj.order_status:
            return APIResponse(data=True)
        else:
            return APIResponse(data=False)

    def post(self, request, *args, **kwargs):
        # 支付宝的post异步回调(沙箱环境下不会回调，上线需要公网IP)
        print(request.query_params)
        print(request.data)
        data = request.data
        signature = data.pop("sign")
        success = alipay.verify(data, signature)
        out_trade_no = data.get('out_trade_no')
        trade_no = data.get('trade_no')
        if success and data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED"):
            models.Order.objects.filter(out_trade_no=out_trade_no).update(
                # 更新流水号，支付状态，支付时间
                trade_no=trade_no, order_status=1, pay_time=datetime.datetime.now()
            )
            log.warning('%s订单支付成功' % out_trade_no)
            return Response('success')
        else:
            log.error('%s订单支付失败' % out_trade_no)
            return Response('fail')
