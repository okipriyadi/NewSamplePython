from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-s', '--okiweb', help="IP address of IFE-API flight server", type=str, default="kyi.priyadi.com")
parser.add_argument('-p', '--okiport', help="Port number ofIFE-API flight server", type=int, default=10000)
parser.add_argument('-c', '--okiclient', help="Client ID", type=int, default=1)
parser.add_argument('-v', '--okiversion', action='version', version='0.0.2')

args = parser.parse_args()
print args.okiweb
print args.okiport
print args.okiclient