"""
If you want to keep track of the tasks' states, Celery needs to store or send the states 
somewhere. There are several built-in result backends to choose from: SQLAlchemy/Django ORM, 
Memcached, Redis, AMQP (RabbitMQ), and MongoDB - or you can define your own.

For this example you will use the rpc result BACKEND, which sends states back as transient 
messages. The backend is specified via the backend argument to Celery, 
(or via the CELERY_RESULT_BACKEND setting if you choose to use a configuration module):

app = Celery('tasks', backend='rpc://', broker='amqp://')
Or if you want to use Redis as the result backend, but still use RabbitMQ as the message broker 
(a popular combination):

app = Celery('tasks', backend='redis://localhost', broker='amqp://')

Now with the result backend configured, let's call the task again. 
This time you'll hold on to the AsyncResult instance returned when you call a task:
The ready()  method returns whether the task has finished processing or not: 
False Lihat di (_3b_ calling and keeping)  
"""
from celery import Celery
app = Celery('_03_keeping_result', backend='rpc://', broker='amqp://')

@app.task
def add(x, y):
    return x + y

"""
Jalankan dengan cara:
=================================================
$ celery -A _03_keeping_result worker --loglevel=info
$ celery -A _01_pendahuluan worker --loglevel=info
=================================================

"""

