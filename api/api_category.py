from api import log
from app import HOST


class ApiCategory:
    # 初始化
    def __init__(self, session):
        # 初始化 session
        self.session = session
        # 商品分类 url
        self.__url_category = HOST + "/api/v1/category/all"
        # 分类下所有商品 url
        self.__url_category_detail = HOST + "/api/v1/product/by_category?id={}"
        # 商品息 url
        self.__url_category_info = HOST + "/api/v1/product/2"

    # 1、获取商品分类 接口封装
    def api_get_category(self):
        result = self.session.get(self.__url_category)
        log.info("获取商品分类接口,请求url为：{} 响应结果为：{}".format(self.__url_category, result.json()))
        return result

    # 2、获取商品分类下商品 接口封装
    def api_get_category_detail(self, category_id):
        result = self.session.get(self.__url_category_detail.format(category_id))
        log.info("获取商品分类下所有商品接口,请求url为：{} 响应结果为：{}".format(self.__url_category_detail, result.json()))
        return result

    # 3、获取商品信息 接口封装
    def api_get_category_info(self):
        result = self.session.get(self.__url_category_info)
        log.info("获取商品信息接口，请求url: {} 响应结果为：{}".format(self.__url_category_info, result.json()))
        return result
