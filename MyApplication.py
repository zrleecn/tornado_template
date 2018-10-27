import torndb
import tornado.web
import os



class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # 渲染变量到模板
        self.write("hello")
        self.application.db.execute("insert into houses(title, position, price, score, comments) values(%s, %s, %s, %s, %s)", "独立装修小别墅", "紧邻文津街", 280, 5, 128)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "statics"),
            debug=True,
        )
        super(Application, self).__init__(handlers, **settings)
        # 创建一个全局mysql连接实例供handler使用
        self.db = torndb.Connection(
            host="127.0.0.1",
            database="tornadotest",
            user="root",
            password="zrlee.cn"
        )


