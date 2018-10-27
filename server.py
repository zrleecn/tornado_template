"""
服务文件

"""

import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
import torndb
import urls
import setting
import redis

# 默认服务器端口
tornado.options.define("port", default=8000, type=int, help="端口号")


# 自定义Application 类
class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        # 向application添加db操作对象
        self.db = torndb.Connection(**setting.mysql_opstions)
        # 添加redis操作对象
        self.redis = redis.StrictRedis(**setting.redis_options)


def main():
    print(tornado.options.options.port)
    tornado.options.options.log_file_prefix = setting.log_path
    tornado.options.options.logging = setting.log_level
    tornado.options.parse_command_line()
    app = Application(
        urls.urls,
        **setting.settings
    )

    app.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
