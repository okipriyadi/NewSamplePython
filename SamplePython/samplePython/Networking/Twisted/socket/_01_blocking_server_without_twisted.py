# This is the blocking version of the Slow Poetry Server.
import os, socket, time
    

def main():
    poetry_file = 'ecstasy.txt'
    num_bytes = 300
    delay = 0.5
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 11002 or 0))
    sock.listen(2)

    print 'Serving %s on port %s.' % (poetry_file, sock.getsockname()[1])
    while True:
        #blocking until client come and accept
        soket, addr = sock.accept()
        print 'Somebody at %s wants poetry!' % (addr,)
        inputf = open(poetry_file)

        nyang_dikirim = True
        while nyang_dikirim:
            bytes = inputf.read(num_bytes)
            if not bytes: # no more poetry :(
                soket.close()
                inputf.close()
                nyang_dikirim = False
             
            if nyang_dikirim:
                print 'Sending %d bytes' % len(bytes)
        
                try:
                    soket.sendall(bytes) # this is a blocking call
                except socket.error:
                    sock.close()
                    inputf.close()
                
                time.sleep(delay)

if __name__ == '__main__':
    main()
