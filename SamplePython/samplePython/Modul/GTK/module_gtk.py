import gtk;
class Base:
    def __init__(self):
        print "membuat window kosong"
        self.windows = gtk.Window( )   
        #mmbuat posisi windows ada di tengah
        self.windows.set_position(gtk.WIN_POS_CENTER)
        #agar ketika windows di close tidak ada masalah apapun dan program akan menutup dengan sendiriya
        self.windows.connect("destroy", self.close_windows)
        #membuat ukuran windows sesuai dengan ukuran
        self.windows.set_size_request(500, 200)
        #membuat ukuran windows sesuai dengan ukuran dengan variabel
        self.window_size = self.window_width, self.window_height =320,450
        self.windows.set_size_request(self.window_width, self.window_height)
        #set title
        self.windows.set_title("Ini Window")
        
        #create button
        self.horizontal_box = gtk.HBox()
        #self.fix_object = gtk.Fixed()
        
        #membuat jarak antar tombol
        self.horizontal_box
        self.tombol = gtk.Button("Tekan saya!")
        self.tombol2 = gtk.Button("saya tombol!")
        
        #self.fix_object.put(self.tombol, 20,50)
        #self.fix_object.put(self.tombol2, 20,90)
        self.horizontal_box.pack_start(self.tombol)
        self.horizontal_box.pack_start(self.tombol2)
        
        self.windows.add(self.horizontal_box)
        
        #show 
        self.windows.show_all()
    def close_windows(self):
        print "anda telah menekan tombol close"
        gtk.main_quit()
        
    def main(self):
        #agar windows terus ada (looping) sampai windows ditekan tombol close
        gtk.main()
        
if(__name__ == "__main__"):
    root = Base()
    root.main()