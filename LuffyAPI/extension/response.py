from rest_framework.response import Response

from LuffyAPI.extension import return_code


class APIResponse(Response):
    def __init__(self, code=return_code.SUCCESS, message='OK', data=None, *args, **kwargs):
        """
        统一格式
        {
            "code": 0,
            "message": "OK",
            "data": None
        }
        """
        res_dict = {'code': code, 'message': message, 'data': data}

        """data为空时不返回data属性"""
        # res_dict = {'code': code, 'message': message}
        # if data:
        #     res_dict = {'code': code, 'message': message, 'data': data}
        res_dict.update(kwargs)
        super().__init__(data=res_dict, *args, **kwargs)
