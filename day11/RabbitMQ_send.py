#-*- coding: utf-8 -*-
#AuthorZhiWenwei
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#声明queue
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',routing_key='hello',body='I love you')
print("[x] sent 'hello world!!!!!!'")
connection.close()