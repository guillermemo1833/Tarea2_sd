import time
import random
import json
import pika
import threading

def camion(id_camion, interval):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()  
    channel.queue_declare(queue='data_queue')

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

        json_data = json.dumps(data)
        print(f"ENVIANDO MENSAJE... - {json_data}" )
        channel.basic_publish(exchange='', routing_key='data_queue', body=json_data)

        time.sleep(interval)

    connection.close()


def main():
    cant_camion = 5
    interval = 5

    for i in range(cant_camion):
        camion_thread = threading.Thread(target=camion, args=(i+1, interval))
        camion_thread.start()

    while True:
        time.sleep(0.1)


if __name__ == "__main__":
    main()
