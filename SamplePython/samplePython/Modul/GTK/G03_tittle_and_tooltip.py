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
        self.window.set_size_request(600, 400)
        #Untuk menampilkan tooltip
        self.window.set_tooltip_text("Ini GUI saya \nini baris kedua")
        
        #membuat tittle 
        self.window.set_title("Ini Judul")
        
        
        self.button1 = gtk.Button("EXIT")
        self.button1.connect("clicked", self.destroy)
        #Untuk menampilkan Tool tip
        self.button1.set_tooltip_text("klik disini untuk menutup")
        
        self.button2 = gtk.Button("hide")
        self.button2.connect("clicked", self.myhide)
        self.button3 = gtk.Button("show")
        self.button3.connect("clicked", self.myshow)
        
        fixed = gtk.Fixed()
        fixed.put(self.button1, 20, 30)
        fixed.put(self.button2, 100, 30)
        fixed.put(self.button3, 200, 30)
        
        self.window.add(fixed)
        self.window.show_all()
        self.window.connect("destroy", self.destroy)
    
    def main(self):  
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()
