"""membaca dan menulis file konfigurasi berformat seperti file 
yg berektention .ini di windows, kita bisa menggunakan library 
ConfigParser yang merupakan library standarnya python."""

import ConfigParser
import io

CONFIG_FILE = 'konpig.ini'
CONFIG_DEFAULT = """
[server]
ip = 0.0.0.0
port = 5050
"""
config = ConfigParser.RawConfigParser()
# tentukan defaultnya
config.readfp(io.BytesIO(CONFIG_DEFAULT))
# lalu di override (timpa) dari file konfigurasi
config.read(CONFIG_FILE)

print "IP :", config.get('server','ip')
print "PORT :", config.get('server','port')

with open(CONFIG_FILE, 'w') as configfile:
    config.write(configfile)
