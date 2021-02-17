import pika, sys, os


def main():
    # opens connection and channel to rabbitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672))
    channel = connection.channel()

    # delcares queue if not already declared
    channel.queue_declare(queue='hello')

    # defines behaviour for when a message is received
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    # sets queue and message behaviour
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    # writes to log and begins monitoring for messages
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)