"""
On the client-side code, we create a client socket using the port argument and connect to the
server. Then, the client sends the message, Test message. This will be echoed to
the server, and the client immediately receives the message back in a few segments. Here,
two try-except blocks are constructed to catch any exception during this interactive session.
"""

import socket
import sys
import argparse


HOST = 'localhost'


def echo_client(port):
    portnya  = port or 10001 
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server
    sock.connect((HOST, portnya))
    
    #send_data
    try:
        message = "tolong kirim teks ini yah"
        sock.sendall(message)
        #look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print "Received: %s" % data
    
    except socket.errno, e:
        print "Socket error: %s" %str(e)
    except Exception, e:
        print "Other exception: %s" %str(e)
    finally:
        print "Closing connection to the server"
        sock.close()
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="socket server example")
    parser.add_argument('--port', action = "store", dest="port", type = int, required = False)
    given_argu = parser.parse_args()
    port = given_argu.port
    print "port =    ", port
    echo_client(port)