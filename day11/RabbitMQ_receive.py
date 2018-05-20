#-*- coding: utf-8 -*-
#AuthorZhiWenwei
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel() #声明一个管道

channel.queue_declare(queue='hello')
def callback(ch,method,properties,body):  #回调函数
    print("ch---",ch,"method---",method,"pro---",properties)
    print("[x] Receviced %r" %body)
channel.basic_consume(callback,queue='hello',no_ack=True) #如果收到消息就调用callback
print("[*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()