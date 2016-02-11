"""
Timeouts
select() also takes an optional fourth parameter which is the number of seconds to wait before breaking 
off monitoring if no channels have become active. Using a timeout value lets a main program call select() 
as part of a larger processing loop, taking other actions in between checking for network input.

When the timeout expires, select() returns three empty lists. Updating the server example to use a 
timeout requires adding the extra argument to the select() call and handling the empty lists after 
select() returns.
=================================================================================================================
    # Wait for at least one of the sockets to be ready for processing
    print >>sys.stderr, '\nwaiting for the next event'
    timeout = 1
    readable, writable, exceptional = select.select(inputs, outputs, inputs, timeout)

    if not (readable or writable or exceptional):
        print >>sys.stderr, '  timed out, do some other work here'
        continue
=================================================================================================================


"""