from StringIO import StringIO
from ConfigParser import SafeConfigParser


output = StringIO()
cfg_parser = SafeConfigParser()
cfg_parser.add_section('certificate')
cfg_parser.set('certificate', 'commonname', "Saya")
cfg_parser.set('certificate', 'not_before', "87")
cfg_parser.set('certificate', 'not_after', "2100")
cfg_parser.set('certificate', 'digest', "12345")
cfg_parser.write(output)
print output
print output.getvalue()



#Simpan output kedala sebuah file
with file("_05_savedisini.ini", 'w') as fpw:
    fpw.write(output.getvalue())
    fpw.flush()