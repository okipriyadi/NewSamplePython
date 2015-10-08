#create celery application tasks

"""
In order to use celery's task queuing capabilities, our first step after installation must be to create a celery instance. This is a simple process of importing the package, creating an "app", and then setting up the tasks that celery will be able to execute in the background.
"""

from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://')

"""
The first argument to the Celery function is the name that will digunakan to tasks to identify them.

The backend parameter is an optional parameter that is necessary if you wish to query the 
status of a background task, or retrieve its results. If your tasks are simply functions that 
do some work and then quit, without returning a useful value  to use in your program, you can leave this
parameter out. If only some of your tasks require this functionality, enable it here and 
we can disable it on a case-by-case basis further on.

The broker parameter specifies the URL needed to connect to our broker. In our case, this is the RabbitMQ service that is running on our server. RabbitMQ operates using a protocol called "amqp". If RabbitMQ is operating under its default configuration, celery can connect with no other information other than the amqp:// scheme.
"""


print "----------------Membuat Tugas ----------------------------------"

@app.task(ignore_result=True)
def print_hello():
    print 'hello there'

"""
Each celery task must be introduced with the decorator @app.task. This allows celery to identify functions that it can add its queuing functions to. After each decorator, we simply create a function that our workers can run.

Because this function does not return any useful information (it instead prints it to the console), we can tell celery to not use the backend to store state information about this task. This is less complicated under the hood and requires fewer resources.

Next, we will add another function that will generate prime numbers. This can be a long-running process, so it is a good example for how we can deal with asynchronous worker processes when we are waiting for a result.
"""


@app.task
def gen_prime(x):
    multiples = []
    results = []
    for i in xrange(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in xrange(i*i, x+1, i):
                multiples.append(j)
    return results

"""
Because we care about what the return value of this function is, and because we want to know when it has completed (so that we may use the results, etc), we do not add the ignore_result parameter to this second task.

Save and close the file.
"""










"""
-----------------------------------
Running the celery worker Server
-----------------------------------
We can now start a worker processes that will be able to accept connections from applications. 
It will use the file we just created to learn about the tasks it can perform.

Starting a worker instance is as easy as calling out the application name with the celery command. 
We will include a "&" character at the end of our string to put our worker process in the background:

buka shell 

$ celery worker -A tasks &


This will start up an application, and then detach it from the terminal, allowing you to continue to use it for other tasks.

-----------------------------------
Calling the task
-----------------------------------
We can use the worker process(es) we spawned to complete work in the background for our programs.

Instead of creating an entire program to demonstrate how this works, we will explore the different options in a Python interpreter:

=============================================
python
=============================================

At the prompt, we can import our functions into the environment:
=============================================
from tasks import print_hello
from tasks import gen_prime
=============================================

If you test these functions, they appear to not have any special functionality. The first function 
prints a line as expected:

=============================================
print_hello()
=============================================

hasilnya:
=============================================
hello there
=============================================

The second function returns a list of prime numbers:
=============================================
primes = gen_prime(1000)
print primes
=============================================

If we give the second function a larger range of numbers to check, 
the execution hangs while it calculates:
=============================================
primes = gen_prime(50000)
=============================================

Stop the execution by typing "CTRL-C". This process is clearly NOT COMPUTING in the background.
To access the background worker, we need to use the .delay method. 
Celery wraps our functions with additional capabilities. This method is used to pass the function 
to a worker to execute. It should return immediately:
=============================================
primes = gen_prime.delay(50000)
=============================================

This task is now being executed by the workers we started earlier. 
Because we configured a backend parameter for our application, we can check the status of the 
computation and get access to the result.

To check whether the task is complete, we can use the .ready method:
=============================================
primes.ready()
=============================================

hasilnya:
=============================================
False
=============================================

A value of "False" means that the task is still running and a result is not available yet. 
When we get a value of "True", we can do something with the answer.
=============================================
primes.ready()
=============================================

hasilnya
=============================================
True
=============================================

We can get the value by using the .get method.
If we have already verified that the value is computed with the .ready method, 
then we can use that method like this:
=============================================
print primes.get()
=============================================

If, however, you have not used the .ready method prior to calling .get, you most likely want to 
add a "timeout" option so that your program isn't forced to wait for the result, which would defeat 
the purpose of our implementation:

print primes.get(timeout=2)

This will raise an exception if it times out, which you can handle in your program.
"""


