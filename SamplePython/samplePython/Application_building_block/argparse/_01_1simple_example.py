import sys
from argparse import ArgumentParser

def daemon_parser():
    parser = ArgumentParser()
    parser.add_argument("command", choices=('start', 'stop', 'restart'), help="daemon action")
    return parser

parser = daemon_parser()
args = parser.parse_args()
print "parser.parse_args = ", args
print "parse.parse_args().command =", args.command
print "sys.argv[1] =", sys.argv[1]
print "parser.prog =", parser.prog
"""
jika kita memasukan argument start maka hasilnya 

parser.parse_args =  Namespace(command='start')
parse.parse_args().command = start
sys.argv[1] = start
parser.prog = _01_1simple_example.py

"""