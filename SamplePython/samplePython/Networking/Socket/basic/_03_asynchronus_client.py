# This is the asynchronous Get Poetry Now! client.
import datetime, errno, optparse, select, socket

def format_address(address):
    host, port = address
    return '%s:%s' % (host or '127.0.0.1', port)

def main():
    #Connect ke server 1
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 10001))
    sock.setblocking(0)

    #Connect ke server 2
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock2.connect(('127.0.0.1', 10002))
    sock2.setblocking(0)

    #Connect ke server 3
    sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock3.connect(('127.0.0.1', 10003))
    sock3.setblocking(0)

    poems = {"sock":"", "sock2":"", "sock3":""}
    sock2task = {"sock":"1", "sock2":"2", "sock3":"3"}
    sockets = [sock, sock2. sock3]

    # we go around this loop until we've gotten all the poetry
    # from all the sockets. This is the 'reactor loop'.

    while sockets :
        rlist, _, _ = select.select(sockets, [], [])
        # rlist is the list of sockets with data ready to read

        for sock in rlist:
            data = ''

            while True:
                try:
                    new_data = sock.recv(1024)
                except socket.error, e:
                    if e.args[0] == errno.EWOULDBLOCK:
                        # this error code means we would have
                        # blocked if the socket was blocking.
                        # instead we skip to the next socket
                        break
                    raise
                else:
                    if not new_data:
                        break
                    else:
                        data += new_data

            # Each execution of this inner loop corresponds to
            # working on one asynchronous task in Figure 3 here:
            # http://krondo.com/?p=1209#figure3

            task_num = sock2task[sock]

            if not data:
                sockets.remove(sock)
                sock.close()
                print 'Task %d finished' % task_num
            else:
                addr_fmt = format_address(sock.getpeername())
                msg = 'Task %d: got %d bytes of poetry from %s'
                print  msg % (task_num, len(data), addr_fmt)

            poems[sock] += data

    for i, sock in enumerate(sockets):
        print 'Task %d: %d bytes of poetry' % (i + 1, len(poems[sock]))




if __name__ == '__main__':
    main()
