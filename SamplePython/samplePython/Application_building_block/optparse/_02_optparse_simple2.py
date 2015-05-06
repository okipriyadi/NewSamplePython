import optparse

usage = """usage: %prog [options] poetry-file

                This is the Slow Poetry Server, blocking edition.
                Run it like this:
                
                  python slowpoetry.py <path-to-poetry-file>
                
                If you are in the base directory of the twisted-intro package,
                you could run it like this:
                
                  python blocking-server/slowpoetry.py poetry/ecstasy.txt
                
                to serve up John Donne's Ecstasy, which I know you want to do.
                """

parser = optparse.OptionParser(usage)

help = "The port to listen on. Default to a random available port."
parser.add_option('--port', type='int', help=help)

help = "The interface to listen on. Default is localhost."
parser.add_option('--iface', help=help, default='localhost')

help = "The number of seconds between sending bytes."
parser.add_option('--delay', type='float', help=help, default=.7)

help = "The number of bytes to send at a time."
parser.add_option('--num-bytes', type='int', help=help, default=10)

options, args = parser.parse_args()

parser.error("hello")
"""
if len(args) != 1:
    parser.error('Provide exactly one poetry file.')

poetry_file = args[0]

if not os.path.exists(args[0]):
    parser.error('No such file: %s' % poetry_file)
"""