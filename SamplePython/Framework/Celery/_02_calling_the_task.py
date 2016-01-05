"""
Calling the task
To call our task you can use the delay() method.

This is a handy shortcut to the apply_async() method which 
gives greater control of the task execution (see Calling Tasks):
"""

from _01_pendahuluan import add
add.delay(4, 4)
add.delay(5, 5)

"""
The task has now been processed by the worker you started earlier, and you can verify that by looking at the workers console output.
Calling a task returns an AsyncResult instance, which can be used to check the state of the task, wait for the task to finish or get its return value (or if the task failed, the exception and traceback). But this isn't enabled by default, and you have to configure Celery to use a result backend, which is detailed in the next section.
"""

"""
[nama].delay sebenarnya shortcut untuk [nama].apply_async()
"""
add.apply_async((6,6))

"""
The latter enables you to specify execution options like the time to run (countdown), 
the queue it should be sent to and so on:
"""
add.apply_async((2, 2), queue='lopri', countdown=10)
"""
In the above example the task will be sent to a queue named lopri and the task will execute, 
at the earliest, 10 seconds after the message was sent.
"""