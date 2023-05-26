
# Rabittmq

Para que funcione el RabittMQ es necesario copiar estos dos codigos en el terminal

```
 docker pull rabbitmq
```

```
 docker run -d --hostname rabbitmq --name my-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:latest
```

