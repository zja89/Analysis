import tornado.ioloop
from tornado.web import StaticFileHandler
import os
import json
from utils.baostock_util import get_history_volume



class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/history_volumes",BSHistoryVolumes),
            (r"/static(.*)", tornado.web.StaticFileHandler)
        ]
        settings = {
            "template_path": "static",
            "static_path": "static",
        }
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        from utils.baostock_util import get_history_volume
        code = "sh.600703"
        prices,volumes = get_history_volume(code=code,sd="2021-01-01",ed="2021-01-29")
        self.render("example.html",prices=prices,volumes=volumes)


class BSHistoryVolumes(tornado.web.RequestHandler):
    def get(self):

        code = "sh.600703"
        prices,volumes = get_history_volume(code=code,sd="2021-01-01",ed="2021-01-29")
        data = json.dumps(dict(prices=prices,volumes=volumes))
        self.write(data)


root = os.path.dirname(__file__)



def make_app():
    # return Application([
    #     # (r"/", MainHandler),
    #     (r"/static/(.*)", StaticFileHandler, {"path": "/static"}),
    #     (r"/(.*)", tornado.web.StaticFileHandler, {"path": root, "default_filename": "index.html"})
    # ])
    return Application()



if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()