#!/usr/bin/env python
import sys

import pika

message = ' '.join(sys.argv[1:]) or 'info: Hello World!'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

connection.close()

print(' [x] Sent %r' % message)
