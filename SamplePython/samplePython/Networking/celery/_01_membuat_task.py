from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y

"""
In this tutorial you will keep everything contained in a single module, 
but for larger projects you want to create a dedicated module.

The first argument to Celery is the name of the current module, this is needed so that names can be 
automatically generated, the second argument is the broker keyword argument which specifies the URL 
of the message broker you want to use, using RabbitMQ here, which is already the default option. 
See Choosing a Broker above for more choices, e.g. for RabbitMQ you can use amqp://localhost, or for 
Redis you can use redis://localhost.

You defined a single task, called add, which returns the sum of two numbers.

You now run the worker by executing our program with the worker argument:

$ celery -A tasks worker --loglevel=info


"""