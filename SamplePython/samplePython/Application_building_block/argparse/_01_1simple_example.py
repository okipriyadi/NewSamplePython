import sys
from argparse import ArgumentParser

def daemon_parser():
    parser = ArgumentParser()
    """
    jika argumen choice diaktifkan maka jika kita menjalankan program tanpa ada argumen atau dengan 
    argumen yang tidak sesuai dengan yang ada di choice, maka akan ada dimunculkan notifikasi
    bahwa choice is wrong.
    
    'perintah','aksi' pada contoh dibawah nantinya menjadi properti untuk 
    mendapatkan hasil aruen yg diinput 
    """ 
    parser.add_argument("perintah", choices=('start', 'stop', 'restart'), help="tuliskan perintah")
    parser.add_argument("argumen_salajengna", help="tuliskan argumen salajengna ")
    return parser

parser = daemon_parser()
args = parser.parse_args()
print "parser.parse_args = ", args
print "parse.parse_args().perintah =", args.perintah
print "parse.parse_args().argumen_salajengna =", args.argumen_salajengna
print "sys.argv[1] =", sys.argv[1]
print "sys.argv[2] =", sys.argv[2]
print "parser.prog =", parser.prog
"""
jika kita memasukan argument start maka hasilnya 

parser.parse_args =  Namespace(command='start')
parse.parse_args().command = start
sys.argv[1] = start
parser.prog = _01_1simple_example.py

"""