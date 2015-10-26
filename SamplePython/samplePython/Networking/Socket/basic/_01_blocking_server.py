"""
kenapa adisebut blocking server, karena  ketika server mengirim pesan kepada satu client, client 
yang lainnya harus menunggu hingga semua pesan terkirim
 
Jalankan dengan cara 
====================================================================================    
python blocking-server/slowpoetry.py --num-bytes 50 --delay 5 --port 10000 -iface localhost
====================================================================================

cara ngetestnya gunakan netcat atau telnet
====================================================================================
netcat localhost 10000
====================================================================================
"""
import optparse, os, socket, time


def parse_args():
    usage = "eg: python blocking-server/slowpoetry.py --num-bytes 50 --delay 5 --port 10000 -iface localhost"
    parser = optparse.OptionParser(usage)
    parser.add_option('--port', type='int', default= 10000, help="The port to listen on. Default to a random available port.")
    parser.add_option('--iface', default='localhost', help="The interface to listen on. Default is localhost.")
    parser.add_option('--delay', type='float', default=.7, help ="The number of seconds between sending bytes.")
    parser.add_option('--num-bytes', type='int', default=10, help="The number of bytes to send at a time.")
    options, args = parser.parse_args()
    poetry_file = ["asddjask1", "asddjask2","asddjaskasdd3","jaskasddjask4", "asddjaskasddjask5", "asddjask6", "asddjask7", "asddjaskasddj8", "askasddjask9", "asddjaskasd10", "djaskasddjask11", "asddjaskasddj12", "askasddjask13", "asddjask14", "asddjaskasddj15", "ask asddjaskas16", "ddjaskasddja17", "asddjaskasddjaskasddjask18"]
    return options, poetry_file


def send_poetry(sock, poetry_file, num_bytes, delay):
    """Send some poetry slowly down the socket."""

    index = 0
    bytes = ""
    while True:
        
        if index <= 17 :
            bytes = poetry_file[index]
            print 'Sending %d bytes' % len(bytes)
        else:
            sock.close()

        try:
            sock.sendall(bytes) # this is a blocking call
        except socket.error:
            sock.close()
            return
        index = index +1
        time.sleep(delay)


def serve(listen_socket, poetry_file, num_bytes, delay):
    while True:
        #program akan berhenti / terblock karena menunggu listen_socket.accept() yaitu menunggu client yang datang
        print "wait for the client ..."
        sock, addr = listen_socket.accept()
        print 'Somebody at %s wants poetry!' % (addr,)
        send_poetry(sock, poetry_file, num_bytes, delay)


def main():
    options, poetry_file= parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((options.iface, options.port or 0))

    sock.listen(5)

    print 'listen on port %s.' % (sock.getsockname()[1])

    serve(sock, poetry_file, options.num_bytes, options.delay)


if __name__ == '__main__':
    main()
