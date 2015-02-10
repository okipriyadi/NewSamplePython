import pygtk, gtk, time
pygtk.require('2.0')


class Timer():
    def __init__(self):
        self.x = 0
        self.Win()
        
    def Win(self):
        print "win"
        self.win = gtk.Window()
        self.win.connect("destroy", lambda q: gtk.main_quit())
        self.box1 = gtk.HBox()
        self.win.add(self.box1)
        self.box1.show()
        
        self.label = gtk.Label(self.x)
        self.box1.pack_start(self.label)
        self.label.show()
        
        self.button1 = gtk.Button("Start")
        self.box1.pack_start(self.button1)
        self.button1.show()
        self.button1.connect("clicked", self.count)
        
        self.win.show()
        
    def count(self,widget):
        while self.x < 10:
            time.sleep(5)
            self.x+=1
            self.label.set_text(str(self.x))
            print self.x
            
def main():
    gtk.main()

if __name__== "__main__" :
    window = Timer()
    main()  
