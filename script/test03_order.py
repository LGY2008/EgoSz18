import requests

from api import log
from api.api_order import ApiOrder


class TestOrder:
    def setup_class(self):
        # 获取session
        self.session = requests.session()
        # 获取ApiOrder对象
        self.order = ApiOrder(self.session)

    def teardown_class(self):
        # 关闭Session
        self.session.close()

    # 1. 获取用户订单列表 接口
    def test01_order_list(self):
        # 调用接口方法
        result = self.order.api_order_list()
        try:
            # 断言 200
            assert 200 == result.status_code
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise

    # 2. 创建订单 接口
    def test02_create_order(self):
        # 调用接口方法
        result = self.order.api_create_order()
        try:
            # 断言 200
            assert 200 == result.status_code
            # 断言 pass
            assert True == result.json().get("pass")
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise

    # 3. 查看订单 接口
    def test03_show_order(self):
        # 调用接口方法
        result = self.order.api_show_order()
        try:
            # 断言 200
            assert 200 == result.status_code
            # 断言 id
            assert 124 == result.json().get("id")
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise
