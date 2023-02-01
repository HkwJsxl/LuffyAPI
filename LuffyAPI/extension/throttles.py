from django.core.cache import cache

from rest_framework.throttling import SimpleRateThrottle
from rest_framework import exceptions
from rest_framework import status

from LuffyAPI.settings import dev
from LuffyAPI.extension import return_code


class ThrottledException(exceptions.APIException):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_code = 'throttled'


class SmsCodeThrottle(SimpleRateThrottle):
    cache = cache
    cache_format = 'throttle_%(scope)s_%(ident)s'
    scope = 'sms_access'
    THROTTLE_RATES = {scope: '1/%sm' % dev.TX_SMS_CODE_EXPIRATION}

    def get_cache_key(self, request, view):
        mobile = request.data.get('mobile')
        ident = mobile
        return self.cache_format % {'scope': self.scope, 'ident': ident}

    def throttle_failure(self):
        wait = self.wait()
        detail = {
            'code': return_code.TOO_MANY_REQUESTS,
            'message': '验证码频率限制.',
            'detail': '验证码{}s内有效,请勿重复发送.'.format(int(wait))
        }
        raise ThrottledException(detail)

    def parse_rate(self, rate):
        """重写：？分钟1次限制"""
        if rate is None:
            return None, None
        num, period = rate.split('/')
        num_requests = int(num)
        duration = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}[period[-1]]
        count = int(period[0:-1])
        return num_requests, count * duration
