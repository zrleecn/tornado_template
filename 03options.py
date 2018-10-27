import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

# 定义服务器监听端口选项
tornado.options.define("port", default=8000, type=int, help="run server on the given port")
# 无意义，演示多值情况
# tornado.options.define("zrlee", default=[], type=str, multiple=True, help="itcast subjects.")
class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("zrlee")

# python 03options.py  --port=9000
if __name__ == "__main__":
    # tornado.options.parse_command_line()
    tornado.options.parse_config_file("./opt_config.py")
    # tornado.options.options.logging = None
    print(tornado.options.options.port)  # 输出端口号
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()
