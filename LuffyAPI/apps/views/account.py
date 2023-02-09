import re
import datetime

from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from authlib.jose import jwt, JoseError

from user import models
from serializers.account import UserLoginSerializer, UserRegModelSerializer, GetSmsSerializer, UserLoginSmsSerializer

from LuffyAPI.extension.mixins import ReCreateModelMixin
from LuffyAPI.extension.response import APIResponse
from LuffyAPI.extension import return_code
from LuffyAPI.extension.throttles import SmsCodeThrottle
from django.conf import settings
from LuffyAPI.extension.logger import log


class UserRegisterView(ReCreateModelMixin, GenericViewSet):
    """
    注册
    ：注册前先接收验证码
    """
    authentication_classes = []
    permission_classes = []
    queryset = models.UserInfo.objects.filter(is_active=True)
    serializer_class = UserRegModelSerializer


class UserLoginView(APIView):
    """登录"""
    authentication_classes = []
    permission_classes = []

    # 用户名、邮箱、手机号密码登录
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return APIResponse(return_code.VALIDATE_ERROR, serializer.errors)
        return APIResponse(data=serializer.context.get('result'))

    # 手机号验证码登录
    def get(self, request, *args, **kwargs):
        serializer = UserLoginSmsSerializer(data=request.query_params)
        if not serializer.is_valid():
            return APIResponse(return_code.VALIDATE_ERROR, serializer.errors)
        return APIResponse(data=serializer.context.get('result'))


class GetSmsView(APIView):
    """发送验证码"""
    authentication_classes = []
    permission_classes = []
    throttle_classes = [SmsCodeThrottle, ]

    def post(self, request, *args, **kwargs):
        serializer = GetSmsSerializer(data=request.data)
        if not serializer.is_valid():
            return APIResponse(return_code.VALIDATE_ERROR, serializer.errors)
        return APIResponse(data=serializer.context.get('result'))


class VerifyEmailView(APIView):
    """邮箱注册"""
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        """
        用于验证邮箱的token,
        并完成相应的确认操作
        """
        token = request.query_params.get('token')
        key = settings.EMAIL_SECRET_KEY
        try:
            data = jwt.decode(token, key)
            email = data.get('operation').get('email')
            password = data.get('operation').get('password')

            expire = data.get('operation').get('expire')
            expire_time = datetime.datetime.strptime(expire, '%Y/%m/%d %X')
            current_time = datetime.datetime.now()
            ret_time = current_time - expire_time  # 0:20:30.401038
            # 过期时间30分钟
            hour = int(str(ret_time).split(':')[0])
            if hour > 0:
                return APIResponse(return_code.AUTH_FAILED, '认证已过期.')
            minute = int(str(ret_time).split(':')[1])
            if minute > 30:
                return APIResponse(return_code.AUTH_FAILED, '认证已过期.')

            models.UserInfo.objects.create_user(username=email, email=email, password=password)
            return APIResponse(data=True)
        except JoseError:
            return APIResponse(data=False, code=return_code.AUTH_FAILED, message='校验失败')
        except Exception as e:
            log.error(str(e))
            return APIResponse(data=False, message='未知错误.%s' % e)

    def post(self, request, *args, **kwargs):
        """
        生成用于邮箱验证的地址
        """
        email = request.data.get('email')
        password = request.data.get('password')
        # 过期时间
        expire = request.data.get('expire')
        user = models.UserInfo.objects.filter(email=email)
        if user:
            return APIResponse(return_code.AUTH_FAILED, '用户已存在,请勿重复使用该邮箱注册或更改邮箱后重新注册.')
        if not email or not password:
            return APIResponse(return_code.VALIDATE_ERROR, '邮箱和密码必填.')
        if not re.match('^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', email):
            return APIResponse(return_code.VALIDATE_ERROR, '邮箱格式错误.')
        if not 8 < len(password) < 18:
            return APIResponse(return_code.VALIDATE_ERROR, '密码长度错误.')
        # 签名算法
        header = {'alg': 'HS256'}
        # 用于签名的密钥
        key = settings.EMAIL_SECRET_KEY
        # 待签名的数据负载
        operation = {
            'email': email,
            'password': password,
            'expire': expire,  # 加入过期时间
        }
        data = {'operation': operation}
        ret = {
            'verify_url': '%s?token=%s' % (
                settings.EMAIL_VERIFY_URL, jwt.encode(header=header, payload=data, key=key).decode('utf-8')
            )
        }
        return APIResponse(data=ret)
