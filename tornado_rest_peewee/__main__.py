# @Author: xiewenqian <int>
# @Date:   2016-09-08T20:53:51+08:00
# @Email:  wixb50@gmail.com
# @Last modified by:   int
# @Last modified time: 2017-01-05T15:36:24+08:00


import tornado.ioloop
import tornado.httpserver
import pyrestful.rest
import click

from tornado_rest_peewee.handlers.teacher import TeacherService


@click.group()
def main():
    pass


@main.command()
@click.option(
    '-p',
    '--port',
    type=int,
    default=8050,
    show_default=True,
    help='服务器监听端口',
)
def runserver(port):
    try:
        # 启动服务器
        click.echo("Start the Web service")
        app = pyrestful.rest.RestService(
            [
                TeacherService,
            ])
        server = tornado.httpserver.HTTPServer(app, xheaders=True)
        server.listen(port)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        click.echo("\nStop the Web service")


if __name__ == '__main__':
    main()
