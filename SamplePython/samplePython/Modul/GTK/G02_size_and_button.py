import pygtk
pygtk.require('2.0')
import gtk

class Base:
    def destroy(self, widget, data=None):
        print "You click the Close Button"
        gtk.main_quit()
        
    def myhide(self, widget):
        self.button1.hide()
    def myshow(self, widget):
        self.button1.show()
        
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER)
        #set posisi
        self.window.set_size_request(600, 400)
        
        #membat button
        self.button1 = gtk.Button("EXIT")
        #sambungkan tombol ini dengan fungsi destroy, sehingga ketika ditekan akan memanggil fungsi destroy
        self.button1.connect("clicked", self.destroy)
        
        self.button2 = gtk.Button("hide")
        self.button2.connect("clicked", self.myhide)
        self.button3 = gtk.Button("show")
        self.button3.connect("clicked", self.myshow)
        fixed = gtk.Fixed()
        #posisi tombol didefinisikan disini
        fixed.put(self.button1, 20, 30)
        fixed.put(self.button2, 100, 30)
        fixed.put(self.button3, 200, 30)
        
        
        
        
        #tambahkan tombol ke container
        self.window.add(fixed)
        #Jika hanya menggunakan self.window.show() maka harus dipanggil satu-satu mulai dari parent, tombol1, tombol2, dst agar lebih praktis gunakan fungsi window.show_all  
        self.window.show_all()
        self.window.connect("destroy", self.destroy)
    def main(self):  
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()
