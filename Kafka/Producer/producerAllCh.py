import time
import random
import json
from kafka import KafkaProducer
import threading

def numero_aleatorio():
    return random.randint(1, 2)



servidores_bootstrap = 'kafka:9092'

# Configuración del productor
producer = KafkaProducer(
    bootstrap_servers=[servidores_bootstrap]  # Dirección y puerto del servidor de Kafka
   
)

def jsonf(id_camion):
    veloc = random.uniform(0, 120)
    bencina = random.uniform(0, 100)
    timestamp = int(time.time())

    data = {
        "Timestamp": timestamp,
        "ID Camion": id_camion,
        "Velocidad": veloc,
        "NivelCombustible": bencina
    }
    return data

# Lista de mensajes y sus correspondientes canales
messages = [
    {'topic': 'camiones_grandes', 'message': 'Mensaje 1'},
    {'topic': 'camiones_chicos', 'message': 'Mensaje 2'},
    {'topic': 'camionetas', 'message': 'Mensaje 3'},
    {'topic': 'vehiculos', 'message': 'Mensaje 4'},
    {'topic': 'motocicletas', 'message': 'Mensaje 5'}
]


for i in range(5):
    data = jsonf(i+1)
    json_data = json.dumps(data)
# Enviar mensajes a los canales correspondientes
    for message in messages:
        topic = message['topic']
        #msg = message['message']
        producer.send(topic, json_data.encode('utf-8'))
        producer.flush()  # Asegurarse de que el mensaje se haya enviado completamente
        #print(f"Mensaje enviado por el canal '{topic}': {msg}")
        print(f"Mensaje enviado por el canal '{topic}'")
        print(f"ENVIANDO MENSAJE... - {json_data}")

# Cerrar conexión
producer.close()
