"""
The SocketServer module is a framework for creating network servers. It defines
classes for handling synchronous network requests (the server request-handler blocks
until the request is completed) over TCP, UDP, UNIX streams, and UNIX datagrams.
It also provides mix-in classes for easily converting servers to use a separate thread or
process for each request.

Responsibility for processing a request is split between a server class and a request-
handler class. 

- server class
  The server deals with the communication issues, such as 
  @ listening on a socket and 
  @ accepting connections, 
- request handler
  request handler deals with the “protocol” issues like 
  @ interpreting incoming data, 
  @ processing it, and 
  @ sending data back to the client.

This division of responsibility means that many applications can use one of the existing
server classes without any modifications and provide a request to communicate with
each other handler class for it to work with the custom protocol.

There are five different server classes defined in SocketServer . 
- BaseServer
  defines the API and is not intended to be instantiated an used directly.
- TCPServer 
  uses TCP/IP sockets to communicate. 
- UDPServer 
  uses datagram sockets.
- UnixStreamServer 
  use UNIX-domain sockets and are only available on UNIX platforms.
- UnixDatagramServer 
  use UNIX-domain sockets and are only available on UNIX platforms.
  
To construct a server, pass it an address on which to listen for requests and a request-
handler class (not instance). The address format depends on the server type and the
socket family used. Refer to the socket module documentation for details.
Once the server object is instantiated, use either handle_request() or
serve_forever() to process requests. The serve_forever() method calls
handle_request() in an infinite loop, but if an application needs to integrate the
server with another event loop or use select() to monitor several sockets for differ-
ent servers, it can call handle_request() directly.
"""

