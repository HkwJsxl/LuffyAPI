# # from ..user.serializers import UserLoginSerializer
# # from ..user import models
# from LuffyAPI.apps.user.serializers import UserLoginSerializer
# from LuffyAPI.apps.user import models
#
# from rest_framework.views import APIView
#
# from LuffyAPI.extension.mixins import ReCreateModelMixin
# from LuffyAPI.extension.response import APIResponse
# from LuffyAPI.extension import return_code
#
#
# class UserLoginView(APIView):
#     """登录"""
#     authentication_classes = []
#     permission_classes = []
#
#     def post(self, request, *args, **kwargs):
#         # 校验数据
#         serializer = UserLoginSerializer(data=request.data)
#         if not serializer.is_valid():
#             return APIResponse(return_code.VALIDATE_ERROR, serializer.errors)
#         # 校验成功，直接返回
#         return APIResponse(data=serializer.context.get('result'))
