import tornado.web
from handler import TestHandler
import os

# class IndexHandler(tornado.web.RequestHandler):
#     def get(self):
#         data = self.application.db.get("select * from houses where id=1")
#         self.write(str(data))
#         self.write("it is work")


urls = [
    (r"/", TestHandler.TestHandler),
    (r"/(.*)", tornado.web.StaticFileHandler,
     dict(path=os.path.join(os.path.dirname(__file__), "html"), default_filename="index.html"))
]
