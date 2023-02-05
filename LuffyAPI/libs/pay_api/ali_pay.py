import os
from django.conf import settings

from alipay import AliPay
from alipay.utils import AliPayConfig

# 加载django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LuffyAPI.settings.dev')
# app_private_key_string = open("/path/to/your/private/key.pem").read()
# alipay_public_key_string = open("/path/to/alipay/public/key.pem").read()

app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
%s
-----END RSA PRIVATE KEY-----""" % settings.ALI_APP_PRIVATE_KEY
alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
%s
-----END PUBLIC KEY-----""" % settings.ALI_ALIPAY_PUBLIC_KEY


def alipay(out_trade_no, subject, goods_price):
    alipay = AliPay(
        appid=settings.ALI_APP_ID,
        app_notify_url=None,  # 默认回调 url
        app_private_key_string=app_private_key_string,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=True,  # 默认 False
        verbose=False,  # 输出调试数据
        config=AliPayConfig(timeout=15)  # 可选，请求超时时间
    )

    # 电脑网站支付，需要跳转到：https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=out_trade_no,
        total_amount=goods_price,
        subject=subject,
        return_url="https://www.luffycity.com/",
        # notify_url="https://www.luffycity.com/notify"  # 可选，不填则使用默认 notify url
    )
    return_url = 'https://openapi.alipaydev.com/gateway.do?%s' % order_string
    print(return_url)


alipay("20161111", 'xiao路飞学城', 99.99)
