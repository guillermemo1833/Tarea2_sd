from kafka import KafkaProducer
from json import dumps
import time

# Inicia el temporizador
start_time = time.time()
#------------------------------------ 

servidores_bootstrap = 'kafka:9092'
topic = 'mi_tema'
productor = KafkaProducer(bootstrap_servers=[servidores_bootstrap])

#------------------------------------ 
i = 0
for k in range(10000):
    productor.send(topic, b'Un mensaje desde Python')
    i = i+1
    print('Enviando: ',i,'  mensaje desde Python')
    #time.sleep(3)
productor.close()
#------------------------------------ 
end_time = time.time()
# Calcula el tiempo transcurrido
elapsed_time = end_time - start_time
# Imprime el tiempo transcurrido
print("Tiempo transcurrido: {:.2f} segundos".format(elapsed_time))
