"""
callLater akan dieksekusi tepat setelah jangka waktu yang diberikan pada parameter pertama dalam contoh ini 1 detik       

 With callLater the callback is the second argument and the first argument is the number of seconds in the future you would like your callback to run. You can use a floating point number to specify a fractional number of seconds, too.

 And Twisted uses timeouts to make sure any "timed callbacks" registered with callLater get called at the right time. Or rather, at approximately the right time. If another callback takes a really long time to execute, a timed callback may be delayed past its schedule.
"""

from twisted.internet import reactor

TRANSFER_EVENT_TIMEOUT = 5
HITUNGAN = 10

def stop_reactor():
    print 'Stop!'    
    reactor.stop()
    

def hallo():
    from time import sleep
    index = 0
    print TRANSFER_EVENT_TIMEOUT 
    watchdog = reactor.callLater(TRANSFER_EVENT_TIMEOUT, stop_reactor)
    if TRANSFER_EVENT_TIMEOUT < HITUNGAN:
        print "ya"
        watchdog.cancel()
        
    while index <= HITUNGAN: 
        print "halo", index
        index = index + 1
        sleep(1)
        
        
    

reactor.callLater(3, hallo)
print 'Start!'
print "tunggu callleter"
reactor.run()



#method yang berguna
#watchdog.called 
#watchdog.cancel() #Untuk Mengcancel
#watchdog.cancelled #mengetahui apakan callleter sudah dicancel
#watchdog.reset(TRANSFER_EVENT_TIMEOUT) #Untuk mereset callLeter degan waktu kembali dari hitungan parameter 1
        