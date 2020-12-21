import requests

from api import log
from api.api_auf import ApiAuf


class TestAuf:
    # 初始化
    def setup_class(self):
        # 获取session
        self.session = requests.session()
        # 获取ApiAuf实例
        self.auf = ApiAuf(self.session)

    # 结束
    def teardown_class(self):
        self.session.close()

    # 验证token测试方法
    def test01_verify_token(self):
        result = self.auf.api_verify_token()
        try:
            # 断言 200
            assert 200 == result.status_code
            # 断言 True
            assert True == result.json().get("isValid")
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise

    # 查询地址方法
    def test02_get_address(self):
        result = self.auf.api_get_address()
        try:
            # 断言 200
            assert 200 == result.status_code
            # 断言 True
            assert "张三" == result.json().get("name")
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise