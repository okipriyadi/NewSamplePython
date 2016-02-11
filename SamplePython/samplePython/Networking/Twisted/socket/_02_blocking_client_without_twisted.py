# This is the blocking Get Poetry Now! client.

import datetime, socket


def main():
    elapsed = datetime.timedelta()
    print 'Task %d: get poetry from server' 
    start = datetime.datetime.now()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost',11002))

    poem = ''

    while True:

        # This is the 'blocking' call in this synchronous program.
        # The recv() method will block for an indeterminate(tidak tentu) period
        # of time waiting for bytes to be received from the server.

        data = sock.recv(1024)

        if not data:
            sock.close()
            break

        poem += data

    time = datetime.datetime.now() - start
    msg = 'Task %d: got %d bytes of poetry from %s in %s'
    print  msg % (1, len(poem), "server1", time)


if __name__ == '__main__':
    main()
