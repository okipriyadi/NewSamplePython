"""
The Celery framework works with the concept of distribution
of work units (tasks) by exchanging messages among the machines that are
interconnected as a network, or local workers. A task is the key concept in Celery;
any sort of job we must distribute has to be encapsulated in a task beforehand.

why use celery

We could justify the use of Celery by listing some of its positive points:
1. It distributes tasks in a transparent way among workers that are spread over the Internet, or local workers
2. It changes, in a simple way, the concurrence of workers through setup (processes, threads, Gevent, Eventlet)
3. It supports synchronous, asynchronous, periodic, and scheduled tasks
4. It re-executes tasks in case of errors

Working with tasks
The client components have the function of creating and dispatching tasks to the brokers.
We will now analyze a code example that demonstrates the definition of a task
by using the @app.task decorator, which is accessible through an instance of
Celery application that, for now, will be called app . 
The following code example demonstrates a simple Hello World app:
========================================================================+
@app.task
def hello_world():
    return "Hello I'm a celery task"
========================================================================+

As we mentioned earlier, there are several types of tasks: synchronous, asynchronous,
periodic, and scheduled. When we perform a task call, it returns an instance of type
AsyncResult . The AsyncResult object is an object that allows the task status to be
checked, its ending, and obviously, its return when it exists. However, to make use
of this mechanism, another component, the result backend, has to be active. This will
be explained further in this chapter. 

To dispatch a task, we should make use of some of the following methods of the task:
1. delay(arg, kwarg=value)     : This is a shortcut to call the apply_async method.
2. apply_async((arg,), {'kwarg': value}) : This allows the setting up of a series of interesting 
   parameters for the execution of the task. Some of them are as follows:
    2.1. countdown : This represents the number of seconds available in the future so that the 
    task execution is started.  The default task is executed immediately.
    2.2 expires : This represents the period of time or date after which a certain task will 
    no longer be executed.
    2.3 retry : In the case of a failure in the connection or sending of a task, 
    this parameter has to be resent. 
    2.4 queue : This is a line to which the task has to be referred.
    2.5 serializer : This represents a data format for the serialization of tasks in disk, 
    and some examples include json , yaml , and others.
    2.6 link : This links one or more tasks to be executed in case the sent task is 
    executed successfully.
    2.7 link_error : This links one or more tasks to be executed in the case of a 
    failure in the execution of the task.
3. apply((arg,), {'kwarg': value}) : This executes a task in the local process in a synchronous way, 
   thereby blocking up to the point a result is ready.

"""






"""
Discovering message transport (broker)
A broker is definitely a key component in Celery. Through it, we get to send and
receive messages and communicate with workers. Celery supports a large number
of brokers. However, to some of these, not all Celery mechanisms are implemented.
The most complete in terms of functionality are RabbitMQ and Redis. A broker has the function
of providing a means of communication between client applications that send tasks
and workers that will execute them. This is done by using task queues. We can have
several network machines with brokers waiting to receive messages to be consumed
by workers.

Understanding workers
Workers are responsible for executing the tasks they have received. Celery displays
a series of mechanisms so that we can find the best way to control how workers will
behave. We can define the mechanisms as follows:
1. Concurrency mode: This is the mode with which workers will perform, for instance, 
processes, threads, Eventlet, and Gevent
2. Remote control: Using this mechanism, we can send messages directly to
a specific worker or a list of them through a high priority queue aiming to
alter their behavior, including runtime
3. Revoking tasks: Using this mechanism, we can instruct one or more workers
to ignore the execution of one or more tasks

Many more features can be set up and even altered in runtime if necessary. For
instance, the number of tasks a worker executes per period of time, from which
queue the workers will consume the most time, and and so on. More information
about workers is available at http://docs.celeryproject.org/en/latest/
userguide/workers.html#remote-control .

Understanding result backends
The result backend component has the role of storing the status and result of the
task to return to the client application. From the result backend supported by Celery,
we can highlight RabbitMQ, Redis, MongoDB, Memcached, among others. Each result
backend listed previously has strong and weak points. Refer to http://docs.
celeryproject.org/en/latest/userguide/tasks.html#task-result-backends
for further information.

Now, we have a general idea of the Celery architecture and its components. So,
let us set up a developing environment that will be used to implement our case studies.
"""
