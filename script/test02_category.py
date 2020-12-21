import requests

from api import log
from api.api_category import ApiCategory


class TestCategory:
    # 初始化
    def setup_class(self):
        # 获取session
        self.session = requests.session()
        # 获取ApiCategory对象
        self.category = ApiCategory(self.session)

    # 结束
    def teardown_class(self):
        # 关闭session
        self.session.close()

    # 1、商品分类 接口测试方法
    def test01_category(self):
        # 调用接口方法
        result = self.category.api_get_category()
        try:
            # 断言 200
            assert 200 == result.status_code
            # 断言 果味
            assert "果味" == result.json()[0].get("name")
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise

    # 2、商品分类下所有商品 接口测试方法
    def test02_category_detail(self, category_id=2):
        # 调用接口方法
        result = self.category.api_get_category_detail(category_id)
        try:
            # 断言 200
            assert 200 == result.status_code
            # 断言 果味
            assert "梨花带雨 3个" == result.json()[0].get("name")
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise

    # 3、商品详情 接口测试方法
    def test03_category_info(self):
        # 调用接口方法
        result = self.category.api_get_category_info()
        try:
            # 断言 200
            assert 200 == result.status_code
            # 断言 果味
            assert "梨花带雨 3个" == result.json().get("name")
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise
