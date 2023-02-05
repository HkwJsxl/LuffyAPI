import re

from django.core.cache import cache

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user import models
from LuffyAPI.settings import dev
from LuffyAPI.libs.tx_sms import send_sms
from LuffyAPI.extension.auth import write_token


class UserRegModelSerializer(serializers.ModelSerializer):
    """
    注册
    """
    password = serializers.CharField(label='密码', min_length=8, max_length=18, write_only=True)
    sms_code = serializers.CharField(label='验证码', write_only=True)

    class Meta:
        model = models.UserInfo
        fields = ('mobile', 'password', 'sms_code')

    def validate(self, attrs):
        mobile = self.initial_data.get('mobile')
        if not re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', mobile):
            raise ValidationError('手机号格式错误.')
        exists = models.UserInfo.objects.filter(mobile=mobile, is_active=True).exists()
        if exists:
            raise ValidationError("手机号已存在,请勿重复注册.")
        else:
            sms_code = self.initial_data.get('sms_code')
            if not sms_code:
                raise ValidationError('请输入验证码.')
            else:
                code = cache.get(dev.TX_SMS_CODE % mobile)
                if not code or sms_code != code:
                    raise ValidationError('验证码校验失败.')
                # 验证码用过后，删除它
                cache.set(dev.TX_SMS_CODE % mobile, '')
        return attrs

    def create(self, validated_data):
        mobile = self.initial_data.get('mobile')
        password = self.initial_data.get('password')
        models.UserInfo.objects.create_user(username=mobile, mobile=mobile, password=password)
        return validated_data


class UserLoginSerializer(serializers.Serializer):
    """
    登录
    考虑：用户名登录时 是否包含手机号和邮箱格式
    """
    username = serializers.CharField(required=False)
    mobile = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        username = self.initial_data.get('username')
        password = self.initial_data.get('password')
        if re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[2567]|7[0-8]|8\d|9[0-35-9])\d{8}$', username):
            # 手机号登录
            user_obj = models.UserInfo.objects.filter(mobile=username, is_active=True).first()
            if not user_obj:
                user_obj = models.UserInfo.objects.filter(username=username, is_active=True).first()
        elif re.match('^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', username):
            # 邮箱登录
            user_obj = models.UserInfo.objects.filter(email=username, is_active=True).first()
            if not user_obj:
                user_obj = models.UserInfo.objects.filter(username=username, is_active=True).first()
        else:
            # 用户名登录
            user_obj = models.UserInfo.objects.filter(username=username, is_active=True).first()
        if not user_obj:
            raise ValidationError('%s 未注册.' % username)
        else:
            is_right = user_obj.check_password(password)
            if not is_right:
                raise ValidationError('密码错误.')
        # 签名
        token = write_token(user_obj)
        # 控制返回格式
        self.context['result'] = {
            'token': token,
            'username': user_obj.username
        }
        return attrs


class UserLoginSmsSerializer(serializers.Serializer):
    """
    登录
    ：手机号验证码登录
    """
    mobile = serializers.CharField()
    sms_code = serializers.CharField()

    def validate(self, attrs):
        mobile = self.initial_data.get('mobile')
        sms_code = self.initial_data.get('sms_code')
        if not re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[2567]|7[0-8]|8\d|9[0-35-9])\d{8}$', mobile):
            raise ValidationError('手机号格式错误.')
        else:
            user_obj = models.UserInfo.objects.filter(mobile=mobile, is_active=True).first()
            if not user_obj:
                raise ValidationError('%s 未注册.' % mobile)
            else:
                code = cache.get(dev.TX_SMS_CODE % mobile)
                if sms_code != code:
                    raise ValidationError('验证码错误或失效.')
            # 签名
            token = write_token(user_obj)
            # 控制返回格式
            self.context['result'] = {
                'token': token,
                'username': user_obj.username
            }
        return attrs


class GetSmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(label='手机号')

    def validate(self, attrs):
        mobile = self.initial_data.get('mobile')
        if not re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', mobile):
            raise ValidationError('手机号格式错误.')
        else:
            send_sms.send(mobile)
            self.context['result'] = {
                'mobile': mobile,
            }
        return attrs
