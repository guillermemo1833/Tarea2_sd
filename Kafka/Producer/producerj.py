from kafka import KafkaProducer
from json import dumps
import time

servidores_bootstrap = 'kafka:9092'
topic = 'mi_tema'

productor = KafkaProducer(bootstrap_servers=[servidores_bootstrap])

while(True):
    productor.send(topic, b'Un mensaje desde Python')
    print('Enviando: Un mensaje desde Python')
    time.sleep(3)
    
# producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
#                          value_serializer=lambda x: 
#                          dumps(x).encode('utf-8'))
