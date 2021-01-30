import tornado.ioloop
from tornado.web import StaticFileHandler
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.render("example.html")

root = os.path.dirname(__file__)

def make_app():
    return tornado.web.Application([
        # (r"/", MainHandler),
        (r"/static/(.*)", StaticFileHandler, {"path": "/static"}),
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": root, "default_filename": "index.html"})
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()