import traceback

from alipay.aop.api.domain.AlipayTradePayModel import AlipayTradePayModel
from alipay.aop.api.domain.GoodsDetail import GoodsDetail
from alipay.aop.api.request.AlipayTradePayRequest import AlipayTradePayRequest
from alipay.aop.api.response.AlipayTradePayResponse import AlipayTradePayResponse


def trade(client, title, subject, goods_id, goods_name):
    # 对照接口文档，构造请求对象
    model = AlipayTradePayModel()
    model.auth_code = "282877775259787048"
    model.body = title
    goods_list = list()
    goods1 = GoodsDetail()
    goods1.goods_id = goods_id
    goods1.goods_name = goods_name
    goods1.price = 99.99
    goods1.quantity = 1
    goods_list.append(goods1)
    model.goods_detail = goods_list
    model.operator_id = "yx_001"
    model.out_trade_no = "20180510AB014"
    model.product_code = "FACE_TO_FACE_PAYMENT"
    model.scene = "bar_code"
    model.store_id = ""
    model.subject = subject
    model.timeout_express = "90m"
    model.total_amount = 1
    request = AlipayTradePayRequest(biz_model=model)
    # 如果有auth_token、app_auth_token等其他公共参数，放在udf_params中
    # udf_params = dict()
    # from alipay.aop.api.constant.ParamConstants import *
    # udf_params[P_APP_AUTH_TOKEN] = "xxxxxxx"
    # request.udf_params = udf_params
    # 执行请求，执行过程中如果发生异常，会抛出，请打印异常栈
    response_content = None
    try:
        response_content = client.execute(request)
    except Exception as e:
        print(traceback.format_exc())
    if not response_content:
        print("failed execute")
    else:
        response = AlipayTradePayResponse()
        # 解析响应结果
        response.parse_response_content(response_content)
        print(response.body)
        if response.is_success():
            # 如果业务成功，则通过respnse属性获取需要的值
            print("get response trade_no:" + response.trade_no)
        else:
            # 如果业务失败，则从错误码中可以得知错误情况，具体错误码信息可以查看接口文档
            print(response.code + "," + response.msg + "," + response.sub_code + "," + response.sub_msg)
