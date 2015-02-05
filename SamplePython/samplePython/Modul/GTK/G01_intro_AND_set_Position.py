import pygtk
pygtk.require('2.0')
import gtk

class Base:
    def destroy(self, widget, data=None):
        print "You click the Close Button"
        gtk.main_quit()
    def __init__(self):
        #untuk membuat instance sekaligus membuat window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        #Untuk menentukan posisi awal kemunculan windows
        #pilihannya
            #1. gtk.WIN_POS_CENTER = posisi tengah 
            #2. gtk.WIN_POS_MOUSE = sesuia posisi mouse kita saat ini
            #3. gtk.WIN_POS_CENTER_ALWAYS = selalu ditengah walau diresize
            #4. gtk_WIN_CENTER_ON_PARENT = ditengah2 objek parentnya
        self.window.set_position(gtk.WIN_POS_MOUSE)
        #walau windows diatas sudah dibuat jika tidak ditampilkan maka akan tetap tersebunyi, oleh karena itu harus di showw
        self.window.show()
        #agar terminal kembali seperti biasa maka jika windows ditutup harus ditutup juga prosesnya
        self.window.connect("destroy", self.destroy)
    def main(self):
        #fungsi utama untuk menampilkan windows
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()
