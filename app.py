from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

items = []

class TodoItems(RequestHandler):
  def get(self):
    self.write({'items': items})

def make_app():
  urls = [("/", TodoItems)]
  return Application(urls, debug=True)
  
if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()