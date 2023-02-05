from django.conf import settings

from .client import alipay


def pay(out_trade_no, subject, total_amount):
    # 电脑网站支付，需要跳转到：https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=out_trade_no,
        total_amount=total_amount,
        subject=subject,
        return_url=settings.RETURN_URL,
        notify_url=settings.NOTIFY_URL
    )
    pay_url = '%s%s' % (settings.ALI_GATEWAY_URL, order_string)
    return pay_url
