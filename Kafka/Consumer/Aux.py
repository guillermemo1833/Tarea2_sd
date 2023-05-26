from kafka import KafkaConsumer


servidores_bootstrap = 'kafka:9092'
topic = 'mi_tema'

consumidor = KafkaConsumer(topic, bootstrap_servers=[servidores_bootstrap])
i = 0
print("Esperando mensajes...")
for msg in consumidor:
    i = i+1
    print(i)
    print(msg.value)
    print("xd")
    
consumidor.close()
print("Mensajes recividos",i)
print("Mensajes perdidos: ",i-100000)