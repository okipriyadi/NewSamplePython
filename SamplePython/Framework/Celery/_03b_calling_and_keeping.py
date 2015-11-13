from _03_keeping_result import add
result = add.delay(4, 4)

#The ready() method returns whether the task has finished processing or not:
print result.ready()

#You can wait for the result to complete, but this is rarely used since it turns the asynchronous call into a synchronous one:
result.get(timeout=1)

#In case the task raised an exception, get() will re-raise the exception, but you can override this by specifying the propagate argument:
result.get(propagate=False)

#If the task raised an exception you can also gain access to the original traceback:
result.traceback
