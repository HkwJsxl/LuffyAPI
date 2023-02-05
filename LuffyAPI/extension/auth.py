import datetime

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from user import models
from LuffyAPI.extension import return_code


class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        if not token:
            raise AuthenticationFailed({'code': return_code.AUTH_FAILED, 'errors': '认证失败!'})
        user_obj = models.UserInfo.objects.filter(token=token).first()
        if not user_obj:
            raise AuthenticationFailed({'code': return_code.AUTH_FAILED, 'errors': '认证失败!'})
        # token过期
        if datetime.datetime.now() > user_obj.token_expiry_date:
            raise AuthenticationFailed({'code': return_code.AUTH_OVERDUE, 'errors': '认证已过期!'})
        return user_obj, token

    def authenticate_header(self, request):
        return 'Bearer realm="API"'


class TokenHeaderAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN')
        if not token:
            raise AuthenticationFailed({'code': return_code.AUTH_FAILED, 'errors': '认证失败!'})
        user_obj = models.UserInfo.objects.filter(token=token).first()
        if not user_obj:
            raise AuthenticationFailed({'code': return_code.AUTH_FAILED, 'errors': '认证失败!'})
        # token过期
        if datetime.datetime.now() > user_obj.token_expiry_date:
            raise AuthenticationFailed({'code': return_code.AUTH_OVERDUE, 'errors': '认证已过期!'})
        return user_obj, token

    def authenticate_header(self, request):
        return 'Bearer realm="API"'


class UserAnonAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN')
        if not token:
            return None, None
        user_obj = models.UserInfo.objects.filter(token=token).first()
        if not user_obj:
            raise AuthenticationFailed({'code': return_code.AUTH_FAILED, 'errors': '认证失败!'})
        # token过期
        if datetime.datetime.now() > user_obj.token_expiry_date:
            raise AuthenticationFailed({'code': return_code.AUTH_OVERDUE, 'errors': '认证已过期!'})
        return user_obj, token

    def authenticate_header(self, request):
        return 'Bearer realm="API"'


def write_token(user_obj):
    payload = jwt_payload_handler(user_obj)
    token = jwt_encode_handler(payload)
    user_obj.token = token
    user_obj.token_expiry_date = datetime.datetime.now() + datetime.timedelta(weeks=2)
    user_obj.save()
    return token
