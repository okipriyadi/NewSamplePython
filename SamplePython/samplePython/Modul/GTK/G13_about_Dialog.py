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
    
    #new Dialog_create by us    
    def about_win(self,widget):
        about = gtk.AboutDialog()
        about.set_program_name("My First GTK Python")
        about.set_version("0.1")
        about.set_copyright("(c) Metalx1000")
        about.set_comments("This Gtk nu Ditulis nganggo Python")
        about.set_website("www.okipriyadi.com")
        about.set_logo(gtk.gdk.pixbuf_new_from_file("google_41.png"))
        about.run()
        about.destroy()
       
    def combo_text(self, widget):
        self.text1.set_text(widget.get_active_text())
        
    def add_combo(self, widget):
        self.combo.append_text(self.text1.get_text())
        
    def textbox(self, widget):
        self.window.set_title(widget.get_text())
        
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_size_request(600, 600)
         
        self.button1 = gtk.Button("EXIT")
        self.button1.connect("clicked", self.destroy)
        
        self.button2 = gtk.Button("hide")
        self.button2.connect("clicked", self.myhide)
        self.button3 = gtk.Button("show")
        self.button3.connect("clicked", self.myshow)
        self.button4 = gtk.Button("relable")
        self.button4.connect("clicked", self.relable)
        self.button5 =gtk.Button("add to Combo box")
        self.button5.connect("clicked", self.add_combo)
        self.button6 = gtk.Button("About")
        self.button6.connect("clicked", self.about_win)
        
        
        self.label1 = gtk.Label("disini dituliskan label")
        
        self.text1 = gtk.Entry()  
        self.text1.connect("changed", self.textbox)
        
        
        self.combo = gtk.combo_box_entry_new_text()
        self.combo.connect("changed", self.combo_text)
        self.combo.append_text("Ini tulisan")
        self.combo.append_text("Opsi 1")
        self.combo.append_text("Opsi 2")
        self.combo.append_text("Opsi 3")
        
        dialog =  gtk.FileChooserDialog("Pilih gambar", None,
                                        gtk.FILE_CHOOSER_ACTION_OPEN,
                                        (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, 
                                        gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)
        filter = gtk.FileFilter()
        filter.set_name("gambar bo")
        filter.add_mime_type("image/png")
        filter.add_mime_type("image/jpg")
        filter.add_pattern("*.png")
        filter.add_pattern("*.jpg")
        filter.add_pattern("*.jpeg")
        dialog.add_filter(filter)
        
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            self.pix = gtk.gdk.pixbuf_new_from_file_at_size(dialog.get_filename(), 200, 200)
            self.image  = gtk.Image()
            self.image.set_from_pixbuf(self.pix)
        elif response == gtk.RESPONSE_CANCEL:
            print "no file selected"
            #exit dari program
            raise SystemExit
        dialog.destroy()
        
        self.box1 = gtk.HBox()       
        self.box1.pack_start(self.button1)
        self.box1.pack_start(self.button2)
        self.box1.pack_start(self.button3)
        self.box1.pack_start(self.button4)
        self.box1.pack_start(self.button6)
        
        self.box3 = gtk.HBox()
        self.box3.pack_start(self.text1)
        self.box3.pack_start(self.button5)
        
        self.box2 =gtk.VBox()
        self.box2.pack_start(self.box1)
        self.box2.pack_start(self.label1)
        self.box2.pack_start(self.box3)
        self.box2.pack_start(self.combo)
        self.box2.pack_start(self.image)
        
        
        self.window.add(self.box2)
        self.window.show_all()
        self.window.connect("destroy", self.destroy)
    
    def main(self):  
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()
