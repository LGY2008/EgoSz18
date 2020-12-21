from app import HOST
from util import GetLog

log = GetLog.get_log()


class ApiIndex:
    #  初始化
    def __init__(self, session):
        # 初始化session
        self.session = session
        log.info("获取session对象：{}".format(session))
        # 轮播图 url
        self.__url_banner = HOST + "/api/v1/banner/1"
        # 专题栏位 url
        self.__url_theme = HOST + "/api/v1/theme?ids=1,2,3"
        # 最新新品 url
        self.__url_product = HOST + "/api/v1/product/recent"

    # 1、轮播图  接口封装
    def api_banner(self):
        log.info("正在调用轮播图接口，请求url: {}".format(self.__url_banner))
        result = self.session.get(self.__url_banner)
        log.info("轮播图请求结果为：{}".format(result.json()))
        return result

    # 2、专题栏位 接口封装
    def api_theme(self):
        log.info("正在调用专题栏位接口，请求url: {}".format(self.__url_theme))
        result = self.session.get(self.__url_theme)
        log.info("专题栏位请求结果为：{}".format(result.json()))
        return result

    # 3、最近新品 接口封装
    def api_new_product(self):
        log.info("最近新品请求结果为，请求url: {}".format(self.__url_product))
        result =  self.session.get(self.__url_product)
        log.info("最近新品请求结果为：{}".format(result.json()))
        return result
