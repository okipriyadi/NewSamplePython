import os, socket, time
    

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 11002 or 0))
    sock.listen(2)

    print 'Server start on port %s.' % (sock.getsockname()[1])
    #while ini diperlukan agar client pada urutan tunggu selanjutnya mendapatkan hasil yang sama
    #jika while ini dihilangkan, client berikutnya tetap meunggu tapi tidak akan mendapatkan connection accept dan juga perintah dibawahnya
    while True:
        soket, addr = sock.accept()
        print 'connection from %s ' % (addr,)
        soket.sendall("hai\n")
        time.sleep(8)
        soket.close()
        
    
    

if __name__ == '__main__':
    main()
