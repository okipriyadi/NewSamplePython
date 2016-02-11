# This is the asynchronous Get Poetry Now! client.

import datetime, errno, optparse, select, socket
def get_poetry(sockets):
    """Download poety from all the given sockets."""

    #membuat dictionary kosong dan menjadikan socket sebagai keynya
    #hailnya kira2 peoms = {"socket1":"","socket2":"","socket3":""}
    poems = dict.fromkeys(sockets, '') # socket -> accumulated poem
    print poems
    

    # socket -> task numbers
    #hasilnya kira2 {"socket1":1,"socket2":2,"socket3":3}
    sock2task = dict([(s, i + 1) for i, s in enumerate(sockets)])
    print sock2task
    
    sockets = list(sockets) # make a copy

    # we go around this loop until we've gotten all the poetry
    # from all the sockets. This is the 'reactor loop'.

    while sockets:
        # this select call blocks until one or more of the
        # sockets is ready for read I/O
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

    return poems


def connect(address):
    """Connect to the given server and return a non-blocking socket."""

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.setblocking(0)
    return sock


def format_address(address):
    host, port = address
    return '%s:%s' % (host or '127.0.0.1', port)


def main():
    addresses = [('localhost',10000),('localhost',10001),('localhost',10002)]
    start = datetime.datetime.now()
    sockets = map(connect, addresses)
    #hasilnya [<socket._socketobject object at 0x7f3524045c20>, <socket._socketobject object at 0x7f3524045c90>, <socket._socketobject object at 0x7f3524045d00>]

    poems = get_poetry(sockets)

    elapsed = datetime.datetime.now() - start

    for i, sock in enumerate(sockets):
        print 'Task %d: %d bytes of poetry' % (i + 1, len(poems[sock]))
        print 'Task %d: %s bytes of poetry' % (i + 1, poems[sock])

    print 'Got %d poems in %s' % (len(addresses), elapsed)
    

if __name__ == '__main__':
    main()
