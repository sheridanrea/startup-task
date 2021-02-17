import pika

# opens connection and channel to rabbitmq
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq', port=5672))
channel = connection.channel()

# delcares queue if not already declared
channel.queue_declare(queue='hello')

# sends message to queue
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

# writes to log and closes connection
print(" [x] Sent 'Hello World!'")
connection.close()