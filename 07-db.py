import tornado.web
import tornado.httpserver
import tornado.httpclient
import tornado.ioloop
import tornado.options
import os
import torndb
import json

tornado.options.define("port", default=8000, type=int, help="端口号")

""""
execute(query, parameters, *kwparameters) 返回影响的最后一条自增字段值
execute_rowcount(query, parameters, *kwparameters) 返回影响的行数

get(query, parameters, *kwparameters) 返回单行结果或None，若出现多行则报错。返回值为torndb.Row类型，是一个类字典的对象，即同时支持字典的关键字索引和对象的属相访问。
query(query, parameters, *kwparameters) 返回多行结果，torndb.Row的列表。

"""


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # 渲染变量到模板
        # self.write("hello")
        id = self.application.db.execute(
            "insert into houses(title, position, price, score, comments) values(%s, %s, %s, %s, %s)", "木屋小别墅",
            "蓝马", 280, 5, 128)
        self.write("last inserted id %d" % id)


class GetOneHandler(tornado.web.RequestHandler):
    def get(self):
        """
           获得一条记录
        """
        info = self.application.db.get("select * from houses where id=1")
        self.write(info['title'] + "--")
        self.write(info['position'])


class GetMoreHandler(tornado.web.RequestHandler):
    def get(self):
        houses = self.application.db.query("select * from houses")
        return self.render("query.html", houses=houses)


class XSRFHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render("xsrf.html")


class CookieHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_secure_cookie("name"):
            self.write(self.get_secure_cookie("name"))
        else:
            self.set_secure_cookie("name", "zrlee", expires_days=10)


class PageHandle(tornado.web.RequestHandler):

    def get_current_user(self):
        return False

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.write("logined")


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        next = self.get_argument("next", "")
        print(next)
        self.write("login page")


class AsyncHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous  # 不关闭连接，也不发送响应
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch("https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=18507584705",
                   callback=self.on_response)

    def on_response(self, response):
        if response.error:
            self.send_error(500)

        else:
            data = response.body
            if data:
                print(data)
                data = data.decode("gbk").split('=')
                data = data[1].strip()
                self.write(data)
            else:
                print("error")

        self.flush()  # 发送响应信息，结束请求处理


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/getone", GetOneHandler),
            (r"/query", GetMoreHandler),
            (r"/cookie", CookieHandler),
            (r"/xsrf", XSRFHandler),
            (r"/login", LoginHandler),
            (r"/page", PageHandle),
            (r"/async", AsyncHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "statics"),
            debug=True,
            cookie_secret="NErLkh7NTGi5U4dCJgy9e4nK8EpR2kr4lv2uzj9qtUc=",
            xsrf_cookies=True,
            login_url="/login",
        )
        super(Application, self).__init__(handlers, **settings)
        # 创建一个全局mysql连接实例供handler使用
        self.db = torndb.Connection(
            host="127.0.0.1",
            database="tornadotest",
            user="root",
            password="zrlee.cn"
        )


if __name__ == '__main__':
    print(tornado.options.options.port)
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()
