"""
Untuk mensetting environment
"""
from fabric.api import env, run


env.hosts = '172.16.191.41'

# Set the username
env.user   = 'avionics'

# Set the password [NOT RECOMMENDED]
#env.password = "your password

def test():
    # Uptime    = Melihat jumlah waktu pemakaian komputer oleh seseorang, terhitung proses reboot terakhir.
    run("uptime")

    # Hostname  = Menampilkan nama komputer
    run("hostname")