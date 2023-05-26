import json
from kafka import KafkaConsumer

#def sucursal(id_sucursal, data):
#    print(f"Sucursal {id_sucursal} - Datos: {data}")


# Configuración del consumidor
consumer = KafkaConsumer(
    bootstrap_servers='kafka:9092',  # Dirección y puerto del servidor de Kafka
    group_id='my-group'  # Identificador del grupo de consumidores
)

# Suscribirse a múltiples topics
topics = ['camiones_grandes', 'camiones_chicos', 'camionetas', 'vehiculos', 'motocicletas']
consumer.subscribe(topics)

sucursales = 3
for i in range(sucursales):
    # Consumir mensajes
   
    for message in consumer:
        data = json.loads(message.value.decode('utf-8'))
        print(f"Mensaje recibido por el canal '{message.topic}'",data)
        

        

# Cerrar conexión
consumer.close()
