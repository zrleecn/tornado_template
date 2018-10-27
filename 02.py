import tornado.web
import tornado.ioloop
import tornado.httpserver


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
    # app.listen(8000)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(8000)
    """
       多进程 
       http_server.start(num_processes=1)方法指定开启几个进程，
       参数num_processes默认值为1，即默认仅开启一个进程；
       如果num_processes为None或者<=0，
       则自动根据机器硬件的cpu核芯数创建同等数目的子进程；如果num_processes>0，
       则创建num_processes个子进程。
    """
    http_server.start(0)
    """
    发现我的linux有10个 02.py进程 难道我的有10核心
    """
    tornado.ioloop.IOLoop.current().start()
