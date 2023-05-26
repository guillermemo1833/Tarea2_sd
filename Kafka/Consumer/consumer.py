
import json
from kafka import KafkaConsumer

def sucursal(id_sucursal, data):
    print(f"Sucursal {id_sucursal} - Datos: {data}")

def main():
    sucursales = 3
    servidores_bootstrap = 'kafka:9092'
    topic = 'camiones_grandes'
    print("Esperando mensajes...")

    consumer = KafkaConsumer(topic, bootstrap_servers=[servidores_bootstrap])

    for i in range(sucursales):
        for message in consumer:
            data = json.loads(message.value.decode('utf-8'))
            sucursal(i + 1, data)



if __name__ == "__main__":
    main()
