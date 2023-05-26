import pika
import json

def sucursal(id_sucursal, data):
    
    print(f"Sucursal {id_sucursal} - Datos: {data}")

def callback(ch, method, properties, body, id_sucursal):
    data = json.loads(body)
    sucursal(id_sucursal, data)

def main():
    sucursales = 3

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='data_queue')

    for i in range(sucursales):
        channel.basic_consume(queue='data_queue', on_message_callback=lambda ch, method, properties, body: callback(ch, method, properties, body, i+1), auto_ack=True)

    channel.start_consuming()

if __name__ == "__main__":
    main()
