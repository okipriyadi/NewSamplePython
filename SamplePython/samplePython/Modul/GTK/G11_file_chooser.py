import pygtk
import gtk

if gtk.pygtk_version < (2,3,90):
    print "please upgrade your pygtk"
    raise SystemExit

#artinya ketika gtk.stock_cancel (tombol cancel) dipilih maka responsenya adalah gtk,Response_cancel
#jika yang dipilih adalah Stock open maka responnya adalah gtk.Response_ok
dialog = gtk.FileChooserDialog("Judul..", None, gtk.FILE_CHOOSER_ACTION_OPEN,( 
                               gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, 
                               gtk.STOCK_OPEN, gtk.RESPONSE_OK))

dialog.set_default_response(gtk.RESPONSE_OK)

#saring tipe file yang ditampilkan
filter = gtk.FileFilter()
filter.set_name("Sadayana File")
filter.add_pattern("*")
dialog.add_filter(filter)

#menjalankan papan
response = dialog.run()

if response == gtk.RESPONSE_OK:
    #mendapatkan nama file yang dipilih
    print dialog.get_filename(), 'selected'
elif response == gtk.RESPONSE_CANCEL:
    print "Closed you did't choose any file"
    
dialog.destroy
