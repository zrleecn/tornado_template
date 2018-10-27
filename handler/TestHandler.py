from .BaseHandler import BaseHandler
import tornado.web


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        # data = self.application.db.get("select * from houses where id=1")
        # self.write(str(data))
        self.write("it is work")

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # data = self.application.db.get("select * from houses where id=1")
        # self.write(str(data))
        self.write("it is work")