"""
Many programs rely on the accurate machine time, such as the make command in UNIX.
Your machine time may be different and need synchronizing with another time server in
your network.

In order to synchronize your machine time with one of the Internet time servers, you can write
a Python client for that. For this, ntplib will be used. Here, the client/server conversation will
be done using Network Time Protocol (NTP). If ntplib is not installed on your machine, you
can get it from PyPI with the following command using pip or easy_install :
$ pip install ntplib

"""

import ntplib
from time import ctime

def print_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
    print ctime(response.tx_time)

if __name__ == '__main__':
    print_time()