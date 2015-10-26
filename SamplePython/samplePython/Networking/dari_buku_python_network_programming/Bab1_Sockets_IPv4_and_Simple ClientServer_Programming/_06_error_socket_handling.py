"""
Jalankan dengan cara :
    $ python 1_7_socket_errors.py -host=<HOST> --port=<PORT> --file=<FILE>
    contoh :
    $ python 1_7_socket_errors.py --host=www.pytgo.org --port=8080 --file=1_7_socket_errors.py
"""

import sys
import socket
import argparse

def main():
    # setup argument parsing
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host', action="store", dest="host", required=False)
    parser.add_argument('--port', action="store", dest="port", type=int, required=False)
    parser.add_argument('--file', action="store", dest="file", required=False)

    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file
    
    # First try-except block -- create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print "Error creating socket: %s" % e
        sys.exit(1)

    # Second try-except block -- connect to given host/port
    try:
        s.connect((host, port))
    except socket.gaierror, e:
        #If you try with a non-existent host, this script will print an address error as follows:
        print "Address-related error connecting to server: %s" % e
        sys.exit(1)
    except socket.error, e:
        #If there is no service on a specific port and if you try to connect to that port, then this will throw a connection timeout error as follows: 
        print "Connection error: %s" % e
        sys.exit(1)

    # Third try-except block -- sending data
    try:
        s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
    except socket.error, e:
        print "Error sending data: %s" % e
        sys.exit(1)

    # Fourth tr-except block -- waiting to receive data from remote host    
    while 1:
        try:
            buf = s.recv(2048)
        except socket.error, e:
            print "Error receiving data: %s" % e
            sys.exit(1)

        if not len(buf):
            break
        
        # write the received data
        sys.stdout.write(buf)

if __name__ == '__main__':
    main()