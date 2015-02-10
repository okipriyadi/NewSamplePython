#threading digunakan agar program bisa menjalankan suatu proses dalam satu waktu (multi tasking)
#bisa disebut juga multi processing
import threading

def main():
    #mengetahui berapa program yang sedang jalan
    print "Jumlah threading yang berjalan", threading.active_count()
    #method active count diatas sebenarnya menghitung method enumerate
    print "semua threading: ", threading.enumerate()
    #Untuk mengetahui thread yang yg sedang berjalan gunakan method dibawah ini
    print "current thread : ", threading.current_thread()

if(__name__ == "__main__"):
    main()