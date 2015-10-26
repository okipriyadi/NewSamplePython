import socket

host_name = socket.gethostname()
print "host-name =", host_name
print "IP address:" , socket.gethostbyname(host_name)
print "==============================="

#harus terhubung ke internet
remote_host = "www.google.co.id"
print "host-name =", remote_host
print "IP address:" , socket.gethostbyname(remote_host)
print "==============================="


#exception
remote_host2 = "www.tak-ada-da.com"
try:
    print "IP address: %s" %socket.gethostbyname(remote_host2)
except socket.error, err_msg:
    print "%s: %s" %(remote_host2, err_msg)
    """
    error no 2 : kemungkinan nama domain memang tidak ada        Name or service not known
    error no 3 : kemungkinan terkendala jaringan
    """