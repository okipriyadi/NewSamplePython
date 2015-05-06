import optparse
import sys
parser = optparse.OptionParser("test")

#parser.add_option('-a', action="store_true", default=False)
#parser.add_option('-b', action="store", dest="b")
#parser.add_option('-c', action="store", dest="c", type="int")
print parser.parse_args(["s","c"])
