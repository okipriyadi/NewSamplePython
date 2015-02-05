import ConfigParser

test = ConfigParser.RawConfigParser()
test.read("tommorow.ini")
print test.sections()

