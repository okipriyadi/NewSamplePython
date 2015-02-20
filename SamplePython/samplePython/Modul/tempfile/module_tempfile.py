from tempfile import TemporaryFile, gettempdir
import tempfile
t = TemporaryFile()
data = 'A simple string of text.'

t.write(data)
# Makes sure the marker is at the start of the file
t.seek(0)
print(t.read())

print tempfile.gettempdir()