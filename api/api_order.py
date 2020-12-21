from api import log
from app import HOST, HEADERS


class ApiOrder:
    # 初始化
    def __init__(self, session):
        # 获取session
        self.session = session
        # 订单列表url
        self.__url_order_list = HOST + "/api/v1/order/by_user?page=1"
        # 创建订单 url
        self.__url_create_order = HOST + "/api/v1/order"
        # 查看订单 url
        self.__url_show_order = HOST + "/api/v1/order/124"

    # 1、 获取用户订单列表 接口封装
    def api_order_list(self):
        result = self.session.get(url=self.__url_order_list, headers=HEADERS)
        log.info("获取用户订单列表接口,请求url为：{} 响应结果为：{}".format(self.__url_order_list, result.json()))
        return result

    # 2、创建订单 接口封装
    def api_create_order(self):
        data = {"products":
                    [{"product_id": 8, "count": 1}, {"product_id": 10, "count": 2}]
                }
        result = self.session.post(url=self.__url_create_order, json=data, headers=HEADERS)
        log.info("创建订单接口,请求url为：{} 响应结果为：{}".format(self.__url_create_order, result.json()))
        return result

    # 3、查看订单 接口封装
    def api_show_order(self):
        result = self.session.get(url=self.__url_show_order, headers=HEADERS)
        log.info("查看订单接口,请求url为：{} 响应结果为：{}".format(self.__url_show_order, result.json()))
        return result
