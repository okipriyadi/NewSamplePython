import threading

def do_this(): 
    print "Ini thread baru"
    
def main():
    #menambah thread baru
    our_thread = threading.Thread(target = do_this())
    #Utuk menjalankan thread nya gnakan method start
    our_thread.start()
    
    print "Jumlah threading yang berjalan", threading.active_count()
    print "semua threading: ", threading.enumerate()
    print "current thread : ", threading.current_thread()

if(__name__ == "__main__"):
    main()