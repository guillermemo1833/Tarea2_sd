import time
import random
import json
from kafka import KafkaProducer
import threading

def camion(id_camion, interval):
    servidores_bootstrap = 'kafka:9092'
    producer = KafkaProducer(bootstrap_servers=[servidores_bootstrap])
    topic = 'data_topic'

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
        print(f"ENVIANDO MENSAJE... - {json_data}")
        producer.send(topic, json_data.encode('utf-8'))

        time.sleep(interval)

    producer.close()


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
