from concurrent.futures import ThreadPoolExecutor
from functools import partial, wraps

import uuid
import time
import tornado.ioloop
import tornado.web
import pyrestful.rest

from tornado_rest_peewee.utils.mylogging import MyLogger
from tornado_rest_peewee.utils.util import ReturnData

EXECUTOR = ThreadPoolExecutor(max_workers=64)


def unblock(f):
    """
    tornado非阻塞使用方法
    """
    @tornado.web.asynchronous
    @wraps(f)
    def wrapper(*args, **kwargs):
        self = args[0]

        def callback(future):
            self.on_return(future.result())
        # 限定接收请求个数
        if EXECUTOR._work_queue.qsize() == 0:
            EXECUTOR.submit(
                partial(f, *args, **kwargs)
            ).add_done_callback(
                lambda future: tornado.ioloop.IOLoop.instance().add_callback(
                    partial(callback, future)))
        else:
            self.set_status(503)
            self.on_return(ReturnData(503, '服务器繁忙'))

    return wrapper


class BaseHandler(pyrestful.rest.RestHandler):
    def initialize(self):
        self.logger = MyLogger.getLogger()
        self.uuid = uuid.uuid4().hex
        self.stime = time.time()
        self.logger.info("[{0}] {1}({2}):{3}".format(self.uuid, self.request.method, self.request.remote_ip, self.request.uri))

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers",
                        "Content-Type, x-requested-with")
        self.set_header('Access-Control-Allow-Methods',
                        'POST, GET, OPTIONS, PUT, DELETE')

    def options(self):
        return None

    def on_return(self, return_data):
        if isinstance(return_data, ReturnData):
            self.write(return_data.value)
            self.finish()
            self.logger.info("[{0}] Success handler request({1}): {2}".format(self.uuid, return_data.code, time.time() - self.stime))
        else:
            self.write(return_data)
            self.finish()
            self.logger.info("[{0}] Success handler request: {1}".format(self.uuid, time.time() - self.stime))
