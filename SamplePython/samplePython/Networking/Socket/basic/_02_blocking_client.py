# This is the blocking Get Poetry Now! client.
import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost',10000))

    poem = ''

    while True:
        # This is the 'blocking' call in this synchronous program. The recv() method will block for an indeterminate period of time waiting for bytes to be received from the server.
        data = sock.recv(1024)
        if not data:
            sock.close()
            break
        poem += data
        print "receive ", data
    
    
    print "full poem: %s" % poem


if __name__ == '__main__':
    main()
