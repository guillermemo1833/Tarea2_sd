
import time
import random
import json
from kafka import KafkaProducer
import threading


def numero_aleatorio():
    return random.randint(1, 2)




def camion(id_camion, interval):
    servidores_bootstrap = 'kafka:9092'
    topic = 'camiones_grandes'
    topic1 = 'camiones_chicos'
    topic2 = 'camionetas'
    topic3 = 'vehiculos'
    topic4 = 'motocicletas'
    
    
    producer = KafkaProducer(bootstrap_servers=[servidores_bootstrap])

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


        # Retorna un numero aleatorio el cual decide por que canal se va a enviar la cola
        sucursal = numero_aleatorio()
        
        if sucursal == 1:
            #-------------------------
            print("-------------------------")        
            json_data = json.dumps(data)
            print("Mensaje enviado por canal: ",topic)
            print(f"ENVIANDO MENSAJE... - {json_data}")
            producer.send(topic, json_data.encode('utf-8'))

        elif sucursal == 2:
            #-------------------------
            print("-------------------------")
            print("Mensaje enviado por canal: ",topic1)
            print(f"ENVIANDO MENSAJE... - {json_data}")
            producer.send(topic1, json_data.encode('utf-8'))

        elif sucursal == 3:
            #-------------------------
            print("-------------------------")
            json_data = json.dumps(data)
            print("Mensaje enviado por canal: ",topic2)
            print(f"ENVIANDO MENSAJE... - {json_data}")
            producer.send(topic2, json_data.encode('utf-8'))

        elif sucursal == 4:
            #-------------------------
            print("-------------------------")        
            json_data = json.dumps(data)
            print("Mensaje enviado por canal: ",topic3)
            print(f"ENVIANDO MENSAJE... - {json_data}")
            producer.send(topic3, json_data.encode('utf-8'))

        elif sucursal == 5:
            #-------------------------
            print("-------------------------")
            json_data = json.dumps(data)
            print("Mensaje enviado por canal: ",topic4)
            print(f"ENVIANDO MENSAJE... - {json_data}")
            producer.send(topic4, json_data.encode('utf-8'))
            #--------------------------

        time.sleep(interval)
    
        #producer.close()


def main():
    cant_camion = 5
    interval = 5

    for i in range(cant_camion):
        camion_thread = threading.Thread(target=camion, args=(i + 1, interval))
        camion_thread.start()


        time.sleep(0.3)


if __name__ == "__main__":
    main()
