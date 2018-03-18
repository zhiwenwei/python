#-*- coding:utf-8 -*-
#Author:Kevin
import optparse
parser = optparse.OptionParser()
parser.add_option("-s","--host",dest="host",help="server binnding host address")
parser.add_option("-p","--port",dest="port",help="server binding port")
(options,args)=parser.parse_args()
print("----",parser.parse_args())
print("参数",options,args)
print(options.port)

