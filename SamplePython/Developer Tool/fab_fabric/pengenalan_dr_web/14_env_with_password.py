"""
Untuk mensetting environment
"""
from fabric.api import env, run
import getpass

env.hosts = '172.16.191.41'

# Set the username
env.user   = 'avionics'


password = getpass.getpass()
env.password = password

def test():
    # Uptime    = Melihat jumlah waktu pemakaian komputer oleh seseorang, terhitung proses reboot terakhir.
    run("uptime")

    # Hostname  = Menampilkan nama komputer
    run("hostname")