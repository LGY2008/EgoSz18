from api import log
from app import HOST, HEADERS


class ApiAuf:
    # 初始化
    def __init__(self, session):
        self.session = session
        # 验证token url
        self.__url_token_verify = HOST + "/api/v1/token/verify"
        # 获取地址 url
        self.__url_address = HOST + "/api/v1/address"

    # 验证token
    def api_verify_token(self):
        # 定义data
        data = {"token": HEADERS.get("token")}
        # 调用post请求
        result = self.session.post(self.__url_token_verify, json=data)
        log.info("验证token接口,请求url为：{} 响应结果为：{}".format(self.__url_token_verify, result.json()))
        return result

    # 获取地址
    def api_get_address(self):
        # 调用get请求
        result = self.session.get(self.__url_address, headers=HEADERS)
        log.info("获取地址接口,请求url为：{} 响应结果为：{}".format(self.__url_address, result.json()))
        return result
