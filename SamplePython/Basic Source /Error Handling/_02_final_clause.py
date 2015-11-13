"""
The finally Clause
Final statement akan selalu dijalankan baik ada error ataupun tidak ada.
biasanya final error dilakukan untuk menutup sebua file, releasing sesuatu yag terkunci, 
menutup koneksi database, dll

When no exception has been raised, the code in the finally suite is executed right
after the try block has completed. If an error does happen, then the finally block still
executes, but does not suppress the exception, which continues to bubble up the call chain
looking for a handler.
"""

def get_mutex():
    pass

def dom_some_stuff():
    pass

def free_mutex():
    pass
    
try:
    get_mutex()
    do_some_stuff()
finally:
    free_mutex()
    
    
###try - finall with exception
try:
    get_mutex()
    do_some_stuff()
except (IndexError, KeyError, AttributeError), e:
    log("ERORR: data retrieval accessing a non-existent element")
finally:
    free_mutex()
    