import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import time
import os
tornado.options.define("port", default=8000, type=int, help="端口号")


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # 渲染变量到模板
        return self.render("index.html", area=100)



class Err404Handler(tornado.web.RequestHandler):

    def get(self):
        self.set_status(404,)


class Err210Handler(tornado.web.RequestHandler):
    """对应/err/210"""
    def get(self):
        self.write("sadfsdfsadfsadf")
        self.set_status(210, "info") # 非标准状态码，设置了reason
        time.sleep(3)
        # 重定向
        self.redirect("/")

class SendHandler(tornado.web.RequestHandler):
    def get(self):
        self.send_error(404)


    def write_error(self, status_code, **kwargs):
        self.write(str(status_code))
        self.write(kwargs.get('content', '404 Not Found'))






if __name__ == '__main__':
    print(tornado.options.options.port)
    current_path = os.path.dirname(__file__)
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(current_path, "statics/html"), "default_filename":"index.html"}),
        (r"/err/404", Err404Handler),
        (r"/err/210", Err210Handler),
        (r"/send/404", SendHandler),
    ], debug=True,
        # 静态文件目录设置为/statics
        static_path=os.path.join(os.path.dirname(__file__), "statics"),
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()
