import requests
from api.api_index import ApiIndex
from util import GetLog

log = GetLog.get_log()


class TestIndex:
    # 初始化
    def setup(self):
        # 获取session对象
        self.session = requests.session()
        # 实例化ApiIndex对象
        self.index = ApiIndex(self.session)

    # 结束
    def teardown(self):
        self.session.close()

    # 1、轮播图接口接口 测试方法
    def test01_banner(self):
        result = self.index.api_banner()
        try:
            # 断言响应状态码
            assert 200, result.status_code
            print("响应结果", result.json())
            # 断言 首页置顶
            assert "首页置顶" == result.json().get("name")
        except Exception as e:
            print("错误原因：", e)
            # 错误原因 写入日志
            log.error(e)
            # 抛异常
            raise
            pass

    # 2、获取专题栏位接口 测试方法
    def test02_theme(self):
        # 调用获取专题栏位接口
        result = self.index.api_theme()
        try:
            # 断言响应状态码
            assert 200, result.status_code
            print("响应结果", result.json())
            # 断言 专题栏位
            assert "专题栏位一" == result.json()[0].get("name")
        except Exception as e:
            print("错误原因：", e)
            # 错误原因 写入日志
            # 抛异常
            log.error(e)

            raise
            pass

    # 3、最近新品接口 测试方法
    def test03_new_product(self):
        # 调用最近新品接口
        result = self.index.api_new_product()
        try:
            # 断言响应状态码
            assert 200, result.status_code
            print("响应结果", result.json())
            # 断言 长度
            assert 15 == len(result.json())
        except Exception as e:
            print("错误原因：", e)
            # 错误原因 写入日志
            log.error(e)
            # 抛异常
            raise
        pass