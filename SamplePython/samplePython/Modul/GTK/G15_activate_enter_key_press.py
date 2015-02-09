import gtk 
from wtforms import widgets
class Base:
    def __init__(self):
        win = gtk.Window()
        win.connect("destroy", lambda w: gtk.main_quit())
        
        box =gtk.VBox()
        entry = gtk.Entry()
        
        win.add(box)
        box.pack_start(entry)
        
        win.show_all()
        entry.connect("activate", self.entry_go)
        
    def entry_go(self, widget):
        print "kamu disini", widget.get_text()
        
    def main(self):
        gtk.main()
        
if __name__=="__main__":
    base = Base()
    base.main()