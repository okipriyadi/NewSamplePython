"""
SELECT
Purpose : Wait for notification that an input or output channel is ready.

select memonitor socket, open file, dan pipe (semua hal yang yang mempunyai
fileno() method dan mereturn -file descriptor). select lebih mudah dibandingkan jika kita 
menggunakan polling loop dalam python menggunakan socket timeout, karena monitoring terjadi padaa layer 
Sistem operasi bukan pada interpreteur.  


setblocking() method to change the blocking flag for a socket. The default value
is 1 , which means to block. Passing a value of 0 turns off blocking. If the socket has
blocking turned off and it is not ready for the operation, then socket.error is raised.
A compromise solution is to set a timeout value for socket operations. Use
settimeout() to change the timeout of a socket to a floating-point value repre-
senting the number of seconds to block before deciding the socket is not ready for the
operation. When the timeout expires, a timeout exception is raised.

Using select()
Python’s select() function is a direct interface to the underlying operating system
implementation. It monitors sockets, open files, and pipes (anything with a fileno()
method that returns a valid file descriptor) until they become readable or writable or
a communication error occurs. select() makes it easier to monitor multiple connec-
tions at the same time, and it is more efficient than writing a polling loop in Python using
socket timeouts, because the monitoring happens in the operating system network layer,
instead of the interpreter.

Note: Using Python’s file objects with select() works for UNIX, but is not
supported under Windows.

