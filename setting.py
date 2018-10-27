import os

# Application 配置参数
settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), 'static'),
    template_path=os.path.join(os.path.dirname(__file__), 'templates'),
    xsrf_cookies=True,
    cookie_secret="0p7I+z6NQye+YFm+QZPyycxvA3Ht902DmGlHe6XwQU4=",
    debug=True
)

# 数据库配置参数
mysql_opstions = dict(
    host="127.0.0.1",
    database="tornadotest",
    user="root",
    password="zrlee.cn"
)

# Redis配置参数
redis_options = dict(
    host="127.0.0.1",
    port=6379
)

# 日志配置
log_path = os.path.join(os.path.dirname(__file__), "logs/log")
log_level = "debug"

# 密码加密密钥
passwd_hash_key = "eLiBEbiDQ+iijLHmblEUD+YlLmZB+US9n1DZIuQSo2M="
