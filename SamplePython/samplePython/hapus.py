import threading

def do_this():
    global x
    
    print "this is first thread!"
    while (x<300):
        x+=1
    print x
    
    
def do_after():
    global x
    print "this is second thread!"
    while (x<600):
        x+=1
    print x
    
def main():
    global x
    x= 0 
     
    our_thread = threading.Thread(target=do_this(), name = "Hiji")
    our_thread.start()
    
    our_next_thread = threading.Thread(target=do_after(), name="dua")
    our_next_thread.start()
    
if (__name__ == "__main__"):
    main()
