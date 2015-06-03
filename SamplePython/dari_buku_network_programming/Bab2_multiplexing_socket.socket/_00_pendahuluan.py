"""
This chapter focuses on improving the socket server performance using a few useful
techniques. Unlike the previous chapter, here we consider multiple clients that will be
connected to the server and the communication can be asynchronous. The server does not
need to process the request from clients in a blocking manner, this can be done independent
of each other. If one client takes more time to receive or process data, the server does not
need to wait for that. It can talk to other clients using separate threads or processes.
In this chapter, we will also explore the select module that provides the platform-specific I/O
monitoring functions. This module is built on top of the select system call of the underlying
operating system's kernel. For Linux, the manual page is located at http://man7.org/
linux/man-pages/man2/select.2.html and can be checked to see the available
features of this system call. Since our socket server would like to interact with many clients,
select can be very helpful to monitor non-blocking sockets. There are some third-party
Python libraries that can also help us to deal with multiple clients at the same time. We have
included one sample recipe of using Diesel concurrent library.

You have decided to write an asynchronous Python socket server application. The server will
not block in processing a client request. So the server needs a mechanism to deal with each
client independently.
Python 2.7 version's SocketServer class comes with two utility classes: ForkingMixIn
and ThreadingMixIn . The ForkingMixin class will spawn a new process for each client
request. This class is discussed in this section. The ThreadingMixIn class will be discussed
in the next section. For more information, you can refer to the Python documentation at
http://docs.python.org/2/library/socketserver.html .

"""

