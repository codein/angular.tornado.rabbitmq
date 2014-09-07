# -*- coding: utf-8 -*-
"""
    Simple sockjs-tornado chat application. By default will listen on port 8080.
"""

import pika
import sockjs.tornado
import tornado.ioloop
import tornado.web
from handlers.web_socket_handler import ChatHandler


if __name__ == "__main__":
    import logging
    logging.getLogger().setLevel(logging.DEBUG)

    # 1. Create chat router
    ChatRouter = sockjs.tornado.SockJSRouter(ChatHandler, '/chat')

    handlers = [
                (r'/favicon.ico', tornado.web.StaticFileHandler, {'path': 'docroot/favicon.ico'}),
                (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'docroot'}),
    ]

    # 2. Create Tornado application
    app = tornado.web.Application(
            handlers + ChatRouter.urls
    )

    # 3. Make Tornado app listen on port 8080
    app.listen(8080)

    # 4. Start IOLoop
    tornado.ioloop.IOLoop.instance().start()
