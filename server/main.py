import tornado.ioloop
from tornado.web import StaticFileHandler
import os
import json
from utils.baostock_util import get_history_volume
from tornado.log import enable_pretty_logging
enable_pretty_logging()

root = os.path.dirname(__file__)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/history_volumes",BSHistoryVolumes),
            (r"/static(.*)", tornado.web.StaticFileHandler),
            (r"/code_list", CodeListHandler),
            (r"/test",TestHandler)
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
        self.render("example.html")


class BSHistoryVolumes(tornado.web.RequestHandler):
    def get(self):

        code = "sh.600703"
        code = "sz.000488"
        code = self.get_argument('code', None)
        sd = self.get_argument('start_date', None)
        ed = self.get_argument('end_date', None)
        code = ".".join(code.split(".")[::-1]).lower()
        print(code,sd,ed)
        if not (code and sd and ed):
            return
        date_list,data = get_history_volume(code=code,sd=sd,ed=ed)
        data = json.dumps(dict(date_list=date_list,data=data))
        self.write(data)


class CodeListHandler(tornado.web.RequestHandler):
    def get(self):
        from settings import code_name
        self.write(code_name)




class TestHandler(tornado.web.RequestHandler):
    def get(self):
        key = self.get_argument('key', None)
        print(key)



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