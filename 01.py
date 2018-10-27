import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    """主路由类"""

    def get(self):
        """对应http的get请求方式"""
        self.write("hello Tornado")

    def post(self):
        """
        对应http的post请请求方式
        """
        pass


if __name__ == "__main__":
    app = tornado.web.Application([
        (r'/', IndexHandler),
    ])
    app.listen(8000)

    tornado.ioloop.IOLoop.current().start()
