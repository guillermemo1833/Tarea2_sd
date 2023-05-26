import time
import random
import json
import threading
import pika


def numero_aleatorio():
    return random.randint(1, 5)

def camion(id_camion, interval):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='direct')

    while True:
        veloc = random.uniform(0, 120)
        bencina = random.uniform(0, 100)
        timestamp = int(time.time())

        data = {
            "Timestamp": timestamp,
            "ID Camion": id_camion,
            "Velocidad": veloc,
            "NivelCombustible": bencina
        }

        sucursal = numero_aleatorio()

        if sucursal == 1:
            routing_key = 'camiones_grandes'
        elif sucursal == 2:
            routing_key = 'camiones_chicos'
        elif sucursal == 3:
            routing_key = 'camionetas'
        elif sucursal == 4:
            routing_key = 'vehiculos'
        else:
            routing_key = 'motocicletas'

        message = json.dumps(data)
        channel.basic_publish(exchange='logs', routing_key=routing_key, body=message)
        print(f"Enviando mensaje: {message} por el canal: {routing_key}")

        time.sleep(interval)

    connection.close()


def main():
    cant_camion = 5
    interval = 5

    for i in range(cant_camion):
        camion_thread = threading.Thread(target=camion, args=(i + 1, interval))
        camion_thread.start()

    while True:
        time.sleep(0.1)


if __name__ == "__main__":
    main()
