from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from user import models
from serializers.account import UserLoginSerializer, UserRegModelSerializer, GetSmsSerializer, UserLoginSmsSerializer

from LuffyAPI.extension.mixins import ReCreateModelMixin
from LuffyAPI.extension.response import APIResponse
from LuffyAPI.extension import return_code
from LuffyAPI.extension.throttles import SmsCodeThrottle


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
