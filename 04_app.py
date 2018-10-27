import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import json

# 定义服务器监听端口选项
tornado.options.define("port", default=8000, type=int, help="服务器端口")


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<a href='" + self.reverse_url('cpp_url') + "'>反向解析url-跳转到cpp</a>")


class SubjectHandler(tornado.web.RequestHandler):
    def initialize(self, subject):
        self.subject = subject

    def get(self):
        # 获得请求参数

        # get_body_argument()就是单独获取post表单的参数
        name = self.get_argument('name', default='')  # get post 参数都可以获取到
        # name = name if name else ''
        self.write(self.subject + "<br>" + "请求参数：" + name)


class InfoHandler(tornado.web.RequestHandler):
    """
    /info
    """

    def get(self):
        host = self.request.host
        method = self.request.method
        uri = self.request.uri
        path = self.request.path
        query = self.request.query
        # body = self.request.body  # 请求提数据
        remote_ip = self.request.remote_ip  # 客户端IP
        print(self.request.headers)
        print(self.request.headers.get("User-Agent"))
        # files = self.request.files  post上传的文件
        self.write("host:%s, method:%s, uri:%s, path:%s, query:%s,"
                   "remote_ip:%s" % (host, method, uri, path, query, remote_ip))


class UserHandler(tornado.web.RequestHandler):
    """
    /userinfo/(.+)/(\d+)
    """

    def get(self, name, age):
        self.write("name:" + name + "<br>" + "age:" + age)


class JsonHandler(tornado.web.RequestHandler):
    """
    /json
    """

    def get(self):
        user = {
            "name": "zrlee",
            "age": "19",
            "subject": "python"
        }
        # self.write(user)  这种方式会自己添加上content-Type： application/json; charset=UTF-8

        # 自己序列化需要手动设置header
        user = json.dumps(user)
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(user)


if __name__ == "__main__":
    print(tornado.options.options.port)
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/info", InfoHandler),
        (r"/userinfo/(.+)/(\d+)", UserHandler),
        (r"/json", JsonHandler),
        # (r"/userinfo/(?P<name>.+)/(?P<age>\d+)", UserHandler),
        (r"/python", SubjectHandler, {"subject": "python"}),
        tornado.web.url(r"/cpp", SubjectHandler, {"subject": "cpp"}, name="cpp_url")
    ], debug=True)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()
