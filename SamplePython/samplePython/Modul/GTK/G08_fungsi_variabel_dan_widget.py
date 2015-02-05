"""
Widget adalah objek yang memanggi fungsi.
misal ketika ada fungsi yang dipanggil oleh objek text1.connect("changed", self.nama_fungsi)
maka ketika kita mendefinisikan fungsi seperti def nama_fungsi(self, widget) 
maka dalam hal ini/dalam kasus ini widget adalah text1
bermanfaat untuk memanggil fungsi yang digunakan oleh berbagai macam objek  sehingga setiap objek tidak perlu membuat fungsi tersendiri

"""

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
        
    def relable(self, widget):
        self.label1.set_text("ubah nama")
    
    #Coba lihat widget disini
    def textbox(self, widget):
        self.window.set_title(widget.get_text())
        
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
        self.button4 = gtk.Button("relable")
        self.button4.connect("clicked", self.relable)
        
        self.label1 = gtk.Label("disini dituliskan label")
        
        self.text1 = gtk.Entry()  
        self.text1.connect("changed", self.textbox)
        
        
        
        self.box1 = gtk.HBox()       
        self.box1.pack_start(self.button1)
        self.box1.pack_start(self.button2)
        self.box1.pack_start(self.button3)
        
        self.box1.pack_start(self.button4)
        
        
        #menambahkan container baru            
        self.box2 =gtk.VBox()
        self.box2.pack_start(self.box1)
        self.box2.pack_start(self.label1)
        self.box2.pack_start(self.text1)
        
        
        self.window.add(self.box2)
        self.window.show_all()
        self.window.connect("destroy", self.destroy)
    
    def main(self):  
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()
