import os
import sys
sys.path.append(os.getcwd())
# 服务器地址
HOST = "http://e.cn"
# 请求信息头
HEADERS = {
    "Content-Type": "application/json",
    "token": "6f99bf580ce8911d57e2e6a382b7484d"
}
# 基础路径
BASE_PATH = os.path.dirname(__file__)