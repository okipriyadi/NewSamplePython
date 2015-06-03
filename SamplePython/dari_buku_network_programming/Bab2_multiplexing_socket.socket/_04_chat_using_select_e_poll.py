import socket
import select
import argparse

SERVER_HOST = 'localhost'
EOL1 = b'\n\n'
EOL2 = b'\n\r\n' 
server_response = b"""HTTP/1.1 200 OK\r\n
                      Date: Mon, 1 Apr 2013 01:01:01 GMT\r\n
                      Content-Type: text/plain\r\nContent-Length: 25\r\n\r\n
                      Hello from Epoll Server!"""
                      
class EpollServer(object):
    """server using E poll"""
    def __init__(self, host = SERVER_HOST, port = 0):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((SERVER_HOST, port))
        self.sock.listen(backlog)
        self.sock.setblocking(0)
        self.sock.setsockopt(socket.IPPROT_TCP, socket.TCP_NODELAY , 1)
        print "started Epoll "
        self.epoll = select.epoll()
        self.epoll.register(self.sock.fileno(), select.EPOLLIN)
        
    def run(self):
        """execute epoll server operation"""
        try:
            connections={}; requests= {}; response={} 
            while True:
                events = self.epoll.poll(1)
                for fileno, event in events:
                    if fileno == self.sock.fileno():
                        connection, address = self.socket.accept()
                        connection.setblocking(0)
                        self.epoll.register(connection.fileno(), select.EPOLLIN)
                        connections[connection.fileno()] = connection
                        requests[connection.fileno()] = b''
                        responses[connection.fileno()] = server_response  
                    elif event & select.EPOLLIN:
                        requests[fileno] += connections[fileno].recv(1024)
                        if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                            self.epoll.modify(fileno, select.EPOLLOUT)
                            print('-'*40 + '\n' + requests[fileno].decode()[:-2])
                    elif event & select.EPOLLOUT:
                        byteswritten = connections[fileno].send(responses[fileno])
                        responses[fileno] = responses[fileno][byteswritten:]
                        if len(responses[fileno]) == 0:
                            self.epoll.modify(fileno, 0)
                            connections[fileno].shutdown(socket.SHUT_RDWR)
                        elif event & select.EPOLLHUP:
                            self.epoll.unregister(fileno)
                            connections[fileno].close()
                            del connections[fileno]
        finally:
            self.epoll.unregister(self.sock.fileno())
            self.epoll.close()
            self.sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example with Epoll')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    server = EpollServer(host=SERVER_HOST, port=port)
    server.run()
                    
        