# from rest_framework.viewsets import GenericViewSet
#
# from LuffyAPI.extension import mixins
# from ..user import models
# from ..user import serializers
#
#
# class UserLoginViewSet(mixins.ReListModelMixin, GenericViewSet):
#     queryset = models.UserInfo.objects.all()
#     serializer_class = serializers.LoginModelSerializer
#

# class UserLoginModelSerializer(serializers.ModelSerializer):
#     # 重写username字段
#     username = serializers.CharField(label='用户名/邮箱/手机号')
#
#     class Meta:
#         model = models.UserInfo
#         fields = ('username', 'password',)
#         extra_kwargs = {
#             'username': {'min_length': 3, 'max_length': 18, 'read_only': True},
#             'password': {'min_length': 3, 'max_length': 18, 'write_only': True},
#         }
#
#     def validate(self, attrs):
#         username = attrs.get('username')
#         password = attrs.get('password')
#
#         if re.match('/^1(3\d|4[5-9]|5[0-35-9]|6[2567]|7[0-8]|8\d|9[0-35-9])\d{8}$/', username):
#             user_obj = models.UserInfo.objects.filter(mobile=username).first()
#         elif re.match('^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', username):
#             user_obj = models.UserInfo.objects.filter(email=username).first()
#         else:
#             models.UserInfo.objects.filter(username=username).exists()
#             user_obj = models.UserInfo.objects.filter(username=username).first()
#         if not user_obj:
#             raise ValidationError('用户不存在.')
#         else:
#             is_right = user_obj.check_password(password)
#             if not is_right:
#                 raise ValidationError('密码错误.')
#         return attrs



