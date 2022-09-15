import pika
# from dotenv import load_dotenv
import os
import json
from app import Song, db
from dotenv import load_dotenv

RABBIT_MQ = os.getenv('RABBIT_MQ')

params = pika.URLParameters(
    RABBIT_MQ + '?heartbeat=10&connection_attempts=3&retry_delay=5')

# params = pika.ConnectionParameters(host=MQ_HOST, port=MQ_PORT, credentials=pika.credentials.PlainCredentials(
#     MQ_USER, MQ_PASSWD), heartbeat_interval=0)
# conn = pika.BlockingConnection(parameters=params)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='reddiget')


def callback(ch, method, properties, body):
    print('Received in reddiget')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'song_created':
        product = Product(
            id=data['id'], title=data['title'], url=data['url'])
        db.session.add(product)
        db.session.commit()
        print('Song Created')

    elif properties.content_type == 'song_updated':
        song = Song.query.get(data['id'])
        product.title = data['title']
        product.image = data['url']
        db.session.commit()
        print('Song Updated')

    elif properties.content_type == 'song_deleted':
        product = Song.query.get(data)
        db.session.delete(song)
        db.session.commit()
        print('Song Deleted')


channel.basic_consume(queue='reddiget',
                      on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
