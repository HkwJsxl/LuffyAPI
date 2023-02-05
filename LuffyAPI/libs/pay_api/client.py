from django.conf import settings

from alipay import AliPay
from alipay.utils import AliPayConfig

app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
%s
-----END RSA PRIVATE KEY-----""" % settings.ALI_APP_PRIVATE_KEY

alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
%s
-----END PUBLIC KEY-----""" % settings.ALI_ALIPAY_PUBLIC_KEY

alipay = AliPay(
    appid=settings.ALI_APP_ID,
    app_notify_url=None,  # 默认回调 url
    app_private_key_string=app_private_key_string,
    alipay_public_key_string=alipay_public_key_string,
    sign_type="RSA2",
    debug=True,
    verbose=False,  # 输出调试数据
    config=AliPayConfig(timeout=15)  # 可选，请求超时时间
)
