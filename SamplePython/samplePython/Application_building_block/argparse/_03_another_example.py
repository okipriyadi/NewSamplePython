import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "action", choices=("runserver", "runfcgi",),
    help="Action")
parser.add_argument(
    "app", help="WSGI application to run e.g. occ.app")
parser.add_argument(
    "-C", "--config", type=str, default="conf/fmp.conf",
    help="Configuration file")
parser.add_argument(
    "-H", "--host", type=str, default="127.0.0.1",
    help="Host name or IP address")
parser.add_argument(
    "-p", "--port", type=int, default=8080,
    help="Port number")
args = parser.parse_args()

print "action = ", args.action
print "app = " , args.app
print "config =", args.config
print "host =", args.host
print "port =", args.port