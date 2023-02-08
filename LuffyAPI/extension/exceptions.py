from rest_framework.views import exception_handler

from LuffyAPI.extension.response import APIResponse
from LuffyAPI.extension import return_code
from LuffyAPI.extension.logger import log


def re_exception_handler(exc, context):
    error_info = 'views:%s, error:%s.' % (context['view'], str(exc))
    log.error(error_info)
    response = exception_handler(exc, context)
    if not response:
        return APIResponse(return_code.EXCEPTION_ERROR, error_info)
    if isinstance(response.data, list):
        return APIResponse(return_code.EXCEPTION_ERROR, response.data)
    else:
        return APIResponse(return_code.EXCEPTION_ERROR, response.data.get('detail') or response.data)
