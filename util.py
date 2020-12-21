import logging.handlers
import os

from app import BASE_PATH


class GetLog:

    logger = None

    @classmethod
    def get_log(cls):
        if cls.logger is None:
            # 1. 获取日志器
            cls.logger = logging.getLogger()
            # 2. 设置日志级别
            cls.logger.setLevel(logging.INFO)
            # 3. 获取处理器（根据时间切割）
            tf = logging.handlers.TimedRotatingFileHandler(filename=BASE_PATH + os.sep + "log" + os.sep + "ego.log",
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            # 4. 获取格式器
            fm = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fmt = logging.Formatter(fm)
            # 5. 将格式器添加到处理器中
            tf.setFormatter(fmt)
            # 6. 将处理器添加到日志器中
            cls.logger.addHandler(tf)
        # 7. 返回处理器
        return cls.logger


if __name__ == '__main__':
    GetLog.get_log().info("信息级别测试！")
    GetLog.get_log().error("error级别测试！")
