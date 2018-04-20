#!/usr/bin/env python
import pika


def callback(ch, method, properties, body):
    print(' [x] %r' % body)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)
channel.basic_consume(callback, queue=queue_name, no_ack=True)

print('  [*] Waiting for logs. To exit press CTRL+C')
channel.start_consuming()
