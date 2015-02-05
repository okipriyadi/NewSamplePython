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
         
        self.button1 = gtk.Button("EXIT")
        self.button1.connect("clicked", self.destroy)
        
        self.button2 = gtk.Button("hide")
        self.button2.connect("clicked", self.myhide)
        self.button3 = gtk.Button("show")
        self.button3.connect("clicked", self.myshow)
        
        #Menambahkan box container
        #Untuk horizontal box gunakan gtk.HBox
        #untuk Vertikal box gunakan gtk.VBox
        self.box1 = gtk.HBox()
        #packing semua dalam container
        self.box1.pack_start(self.button1)
        self.box1.pack_start(self.button2)
        self.box1.pack_start(self.button3)
        
        self.window.add(self.box1)
        self.window.show_all()
        self.window.connect("destroy", self.destroy)
    
    def main(self):  
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()
