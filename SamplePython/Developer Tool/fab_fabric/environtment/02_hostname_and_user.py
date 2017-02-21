"""
Untuk mensetting environment
"""
from fabric.api import env, run


env.hosts = 'gcp-build.gcplocal.net'

# Set the username
env.user   = 'gcp'
#env.password = "geta8080@GCP"
# Set the password [NOT RECOMMENDED]
#env.password = "your password

def test():
    # Uptime    = Melihat jumlah waktu pemakaian komputer oleh seseorang, terhitung proses reboot terakhir.
    run("uptime")

    # Hostname  = Menampilkan nama komputer
    run("hostname")