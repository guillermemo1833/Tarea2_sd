import pika
import json


def process_message(channel, method, properties, body):
    data = json.loads(body)
    channel_name = method.routing_key  # Obtener el nombre del canal
    print(f"Mensaje recibido desde el canal '{channel_name}': {data}")
    channel.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='direct')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='logs', queue=queue_name, routing_key='camiones_grandes')
    channel.queue_bind(exchange='logs', queue=queue_name, routing_key='camiones_chicos')
    channel.queue_bind(exchange='logs', queue=queue_name, routing_key='camionetas')
    channel.queue_bind(exchange='logs', queue=queue_name, routing_key='vehiculos')
    channel.queue_bind(exchange='logs', queue=queue_name, routing_key='motocicletas')

    channel.basic_consume(queue=queue_name, on_message_callback=process_message)

    print("Esperando mensajes...")
    channel.start_consuming()


if __name__ == "__main__":
    main()
