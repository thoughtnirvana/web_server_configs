#!/usr/bin/env python
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import app

# Initialize app and serve.
http_server = HTTPServer(WSGIContainer(app.init()))
http_server.bind(8080, '127.0.0.1')
http_server.start(0)
IOLoop.instance().start()
