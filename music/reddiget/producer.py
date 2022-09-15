import pika
import json
import os
from dotenv import load_dotenv
load_dotenv('.env')

RABBIT_MQ = os.getenv('RABBIT_MQ')

params = pika.URLParameters(
    RABBIT_MQ)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body, to_queue):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange='', routing_key=to_queue, body=json.dumps(body), properties=properties)
    # print(" [x] Sent %r" % body)
