"""pip install alipay-sdk-python"""
import os
from django.conf import settings

# 加载django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LuffyAPI.settings.dev')
import logging

from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient

from django.conf import settings
from app_pay import app
from page_pay import page
from trade_pay import trade

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a', )
logger = logging.getLogger('')


def alipay(title, goods_id, goods_name, subject, body, out_trade_no, merchant_id):
    """
    设置配置，包括支付宝网关地址、app_id、应用私钥、支付宝公钥等，其他配置值可以查看AlipayClientConfig的定义。
    """
    alipay_client_config = AlipayClientConfig()
    alipay_client_config.server_url = settings.ALI_SERVER_URL
    alipay_client_config.app_id = settings.ALI_APP_ID
    alipay_client_config.app_private_key = settings.ALI_APP_PRIVATE_KEY
    alipay_client_config.alipay_public_key = settings.ALI_ALIPAY_PUBLIC_KEY

    """
    得到客户端对象。
    注意，一个alipay_client_config对象对应一个DefaultAlipayClient，定义DefaultAlipayClient对象后，alipay_client_config不得修改，如果想使用不同的配置，请定义不同的DefaultAlipayClient。
    logger参数用于打印日志，不传则不打印，建议传递。
    """
    client = DefaultAlipayClient(alipay_client_config=alipay_client_config, logger=logger)
    # page(client, merchant_id, out_trade_no, subject, body)
    trade(client, title, subject, goods_id, goods_name)
    # app(client,out_trade_no,subject,body)


alipay('title', '2088722007435611', 'goods_name', 'subject', 'body', '20150320010101003', '2088722007435606')
