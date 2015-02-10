import threading


def do_this(): 
    global dead
    print "Ini thread baru"
    print dead 
    
    x = 0
    """
    while( not dead ):
        x +=1
        pass
    """
    print x
    
def main():
    global dead 
    dead = False
    our_thread = threading.Thread(target = do_this())
    our_thread.start()
    
    print "Jumlah threading yang berjalan", threading.active_count()
    print "semua threading: ", threading.enumerate()
    print "thread is alive  : ", our_thread.is_alive()
    
    #raw_input("Hit Enter to die :")
    dead = True
    print dead
    
if(__name__ == "__main__"):
    main()