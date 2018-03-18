#!/usr/bin/env python
# _*_coding:utf-8_*_
#Author:ZhiWenwei
import optparse
import socketserver
from core.ftp_server import FTPHandler
from conf import settings

class ArgvHandler(object):
    def __init__(self):
        self.parser = optparse.OptionParser()
        # parser.add_option("-s", "--host", dest = "host", help = "server binding host address")
        # parser.add_option("-p", "--port", dest = "port", help = "server binding port")
        (options, args) = self.parser.parse_args()

        self.verify_args(options, args)

    def verify_args(self, options, args):
        '''
        检验并调用相应的功能
        '''
        if not args:
            print("Please use args 'start'")
            return

        if hasattr(self, args[0]):
            func = getattr(self, args[0])
            func()
        else:
            self.parser.print_help()

    def start(self):
        print('---- going to start server ----')
        server = socketserver.ThreadingTCPServer((settings.HOST, settings.PORT), FTPHandler)
        server.serve_forever()
