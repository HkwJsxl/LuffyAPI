"""
sdk：
https://github.com/tencentcloud/tencentcloud-sdk-python#%E9%80%9A%E8%BF%87-pip-%E5%AE%89%E8%A3%85%E6%8E%A8%E8%8D%90
"""

import random

from django.core.cache import cache

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.sms.v20210111 import sms_client, models

from LuffyAPI.settings import dev
from LuffyAPI.extension.logger import log


def send_api(mobile, code):
    try:
        cred = credential.Credential(dev.TX_SMS_ID, dev.TX_SMS_KEY)
        client = sms_client.SmsClient(cred, "ap-guangzhou")
        req = models.SendSmsRequest()

        req.SmsSdkAppId = dev.TX_SMS_SDK_APP_ID
        req.SignName = dev.TX_SMS_SIGN_NAME
        req.TemplateId = dev.TX_SMS_TEMPLATE_ID
        # 模板参数
        req.TemplateParamSet = [code, dev.TX_SMS_CODE_EXPIRATION]

        req.PhoneNumberSet = ["+86%s" % mobile]
        req.SessionContext = ""
        req.ExtendCode = ""
        req.SenderId = ""
        client.SendSms(req)
        # 缓存
        cache.set(dev.TX_SMS_CODE % mobile, code, int(dev.TX_SMS_CODE_EXPIRATION) * 60)

        log.info('%s 发送验证码成功,验证码为 %s' % (mobile, code))

    except TencentCloudSDKException as err:
        log.error('%s 发送验证码失败,错误信息 %s' % (mobile, str(err)))


def rand_code():
    code_str = ''
    for num in range(4):
        code_str += str(random.randint(0, 9))
    return code_str


def send(mobile):
    code = rand_code()
    send_api(mobile, code)
    return code
