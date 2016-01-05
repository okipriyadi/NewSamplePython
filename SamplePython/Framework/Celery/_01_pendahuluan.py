"""
langkah-langkah
1. Choosing and installing a message transport (broker) (rabit-MQ, mongo-DB, etc). 
2. Installing Celery and creating your first task.
3. Starting the worker and calling tasks.
4. Keeping track of tasks as they transition through different states, and inspecting return values.

kita asumsikan bahwa broker dan celery sudah diiinstal (pip install celery). Dan broker sudah dijalnkan. untuk contoh ini 
kita menggunakan broker rabbitmq, untuk menjalankannya bisa menggunakan

$ rabbitmq-server
# or you can start in the background with
$ rabbitmq-server -detached 
maka kita akan membuat first task

Langkah pertama dalam membuat task adalah buat instance nya, 
kita akan panggil "celery application" atau  "app" untuk lebih singkatnya. 
Since this instance is used as the entry-point for everything you want to do in Celery, 
like creating tasks and managing workers, it must be possible for other modules to import it.

In this tutorial you will keep everything contained in a single module,
but for larger projects you want to create a dedicated module.

Let's create the file tasks.py:

"""

from celery import Celery

app = Celery('_01_pendahuluan', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y

"""
The first argument to Celery is the name of the current module, this is needed so that names 
can be automatically generated, the second argument is the broker keyword argument which 
specifies the URL of the message broker you want to use, using RabbitMQ here, which is 
already the default option. See Choosing a Broker above for more choices, 
e.g. for RabbitMQ you can use amqp://localhost, or for Redis you can use redis://localhost.

You defined a single task, called add, which returns the sum of two numbers.

RUNNING CELERY
You now run the worker by executing our program with the worker argument:
buka console baru masuk ke folder dimana file ini berada coba ketik
=================================================
$ celery -A _01_pendahuluan worker --loglevel=info
=================================================

"""

