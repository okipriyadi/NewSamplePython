"""
select            : Wait for I/O Efficiently
Purpose           : Wait for notification that an input or output channel is ready.
Python Version    : 1.4 and later

modul select menyediakan akses ke fungsi monitoring Input / Output . 
modul ini tersedia baik pada UNIX maupun juga pada windows.
modul ini juga memasukan poll(), yang hanya berkerja di UNIX, dan beberapa opsi yang hanya berkerja di variant UNIX

fungsi select() adalah sebagai antarmuka langsung ke implementasi sistem operasi yang mendasarinya. 
fungsi ini memonitor sockets, open files, dan pipes (anything with a fileno() method that returns 
a valid file descriptor) sampai  mereka siap menjadi :
1. readable 
2. writable, or 
3. a communication error occurs. 

membuat lebih mudah untuk memantau beberapa koneksi pada waktu yang sama, dan lebih efisien 
daripada menulis polling loop di Python menggunakan socket timeouts, karena monitoring terjadi
di dalam sistem operasi network layer. bukan pda interpreter

contoh echo server berikut dapat digunakan untuk memonitor lebih dari satu koneksi dalam satu 
waktu menggunakan select() 

pertama-tama buat non-blocking server.
===========================================================================================
    import select
    import socket
    import sys
    import Queue
    
    # Create a TCP/IP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(0)
    
    # Bind the socket to the port
    server_address = ('localhost', 10000)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    server.bind(server_address)
    
    # Listen for incoming connections
    server.listen(5)
===========================================================================================

Argumen select() adalah 3 buah list yang menggandung saluran komunikasi untuk dimonitor:
1. sebuah list  untuk di check pada data yang masuk untuk dibaca
2. sebuah objek yang akan mendapatkan data yang akan dikirim ketika ada tempat di buffer 
3. kemungkinan error (biasanya kombinasi antara saluran input dan output). 

Langkah selanjutnya adalah mensetup list input & output:
===========================================================================================
    # Sockets from which we expect to read
    inputs = [ server ]
    
    # Sockets to which we expect to write
    outputs = [ ]
===========================================================================================

koneksi ditambahkan ke dan dihapus dari list ini oleh server main loop. 

server ini akan menunggu sebuah soket untuk bisa di tulis sebelum mengirimkan data.
setiap koneksi output membutuhkan sebuah queue (antrian) untuk bertindak sebagai 
buffer untuk data yang dikirimkan melalui koneksi itu.

===========================================================================================
    # Outgoing message queues (socket:Queue)
    message_queues = {}
===========================================================================================

panggil select() untuk memblok dan menunggu aktifitas jaringan.

===========================================================================================
  while inputs:
    # Wait for at least one of the sockets to be ready for processing
    print >>sys.stderr, '\nwaiting for the next event'
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
===========================================================================================
select() menghasilkan 3 buah list baru. 
1. semua soket dalam list yang readable mempunyai  data yang masuk di dalam buffer dan 
   tersedia untuk dibaca. 
2. semua soket yang berada di list writable  mempunyai ruang kosong di dalam buffer mereka  
   dan kita dapat menulis kedalamnya
3. socket me-return error jika terjadi error

readable socket merepresentasikan tiga kemungkinan, :
1. jika soket adalah "server" utama (yaitu soket yang digunakan untuk listen) maka kondisi 
   readable berarti soket siap untuk menerima koneksi lainnya. Selain menambahkan sambungan baru
   ke daftar input yang dipantau, bagian ini menetapkan agar soket klien untuk tidak di block.
   kondisi ini terjadi ketika client baru terhubung dan membutuhkan accept dari server. 
 

    ===========================================================================================
        # Handle inputs
        for s in readable:
    
            if s is server:
                # A "readable" server socket is ready to accept a connection
                connection, client_address = s.accept()
                print >>sys.stderr, 'new connection from', client_address
                connection.setblocking(0)
                inputs.append(connection)
    
                # Give the connection a queue for data we want to send
                message_queues[connection] = Queue.Queue()
    ===========================================================================================

2.  Kasus selanjutnya ada menstabilkan koneksi dengan sebuah client yang telah mengirimkan data
    data dibaca menggunakan recv(), kemudian ditempatkan di queue jadi data dapat dikirim 
    melalui soket tersebut dan kembali ke client.
    kondisi ini terjadi ketika client sudah terhubung(terjadi accept pada nomor 1) dan client mengirimkan
    data kepada server
    ===========================================================================================
            else:
                data = s.recv(1024)
                if data:
                    # A readable client socket has data
                    print >>sys.stderr, 'received "%s" from %s' % (data, s.getpeername())
                    message_queues[s].put(data)
                    # Add output channel for response
                    if s not in outputs:
                        outputs.append(s)
    ===========================================================================================
3. sebuah soket tanpa data yg availabel berarti client telah terputus dan stream siap untuk di close.
   kondisi ini terjadi ketika client menutup koneksi
    ===========================================================================================
            else:
                # Interpret empty result as closed connection
                print >>sys.stderr, 'closing', client_address, 'after reading no data'
                # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
    ===========================================================================================

4. ada beberapa kasus untuk koneksi writable. Jika ada data dalam antrian, 
pesan selanjutnya dikirimkan. Jika tidak koneksi di remove dari list output sehingga kedepannya
loop select() tidak mengindikasikan bahwa soket tersebut tersedia untuk dikirimkan
 
===========================================================================================
    # Handle outputs
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except Queue.Empty:
            # No messages waiting so stop checking for writability.
            print >>sys.stderr, 'output queue for', s.getpeername(), 'is empty'
            outputs.remove(s)
        else:
            print >>sys.stderr, 'sending "%s" to %s' % (next_msg, s.getpeername())
            s.send(next_msg)
===========================================================================================
Finally, if there is an error with a socket, it is closed.
===========================================================================================
    # Handle "exceptional conditions"
    for s in exceptional:
        print >>sys.stderr, 'handling exceptional condition for', s.getpeername()
        # Stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
===========================================================================================

The example client program uses two sockets to demonstrate how the server with select() 
manages multiple connections at the same time. The client starts by connecting each TCP/IP 
socket to the server.

===========================================================================================
    import socket
    import sys
    
    messages = [ 'This is the message. ',
                 'It will be sent ',
                 'in parts.',
                 ]
    server_address = ('localhost', 10000)
    
    # Create a TCP/IP socket
    socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM),
              socket.socket(socket.AF_INET, socket.SOCK_STREAM),
              ]
    
    # Connect the socket to the port where the server is listening
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    for s in socks:
        s.connect(server_address)
===========================================================================================

Then it sends one pieces of the message at a time via each socket, and reads all responses available after writing new data.
===========================================================================================
    for message in messages:

        # Send messages on both sockets
        for s in socks:
            print >>sys.stderr, '%s: sending "%s"' % (s.getsockname(), message)
            s.send(message)
    
        # Read responses on both sockets
        for s in socks:
            data = s.recv(1024)
            print >>sys.stderr, '%s: received "%s"' % (s.getsockname(), data)
            if not data:
                print >>sys.stderr, 'closing socket', s.getsockname()
                s.close()
===========================================================================================
Run the server in one window and the client in another. The output will look like this, with different port numbers.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    $ python ./select_echo_server.py
    starting up on localhost port 10000
    
    waiting for the next event
    new connection from ('127.0.0.1', 55821)
    
    waiting for the next event
    new connection from ('127.0.0.1', 55822)
    received "This is the message. " from ('127.0.0.1', 55821)
    
    waiting for the next event
    sending "This is the message. " to ('127.0.0.1', 55821)
    
    waiting for the next event
    output queue for ('127.0.0.1', 55821) is empty
    
    waiting for the next event
    received "This is the message. " from ('127.0.0.1', 55822)
    
    waiting for the next event
    sending "This is the message. " to ('127.0.0.1', 55822)
    
    waiting for the next event
    output queue for ('127.0.0.1', 55822) is empty
    
    waiting for the next event
    received "It will be sent " from ('127.0.0.1', 55821)
    received "It will be sent " from ('127.0.0.1', 55822)
    
    waiting for the next event
    sending "It will be sent " to ('127.0.0.1', 55821)
    sending "It will be sent " to ('127.0.0.1', 55822)
    
    waiting for the next event
    output queue for ('127.0.0.1', 55821) is empty
    output queue for ('127.0.0.1', 55822) is empty
    
    waiting for the next event
    received "in parts." from ('127.0.0.1', 55821)
    received "in parts." from ('127.0.0.1', 55822)
    
    waiting for the next event
    sending "in parts." to ('127.0.0.1', 55821)
    sending "in parts." to ('127.0.0.1', 55822)
    
    waiting for the next event
    output queue for ('127.0.0.1', 55821) is empty
    output queue for ('127.0.0.1', 55822) is empty
    
    waiting for the next event
    closing ('127.0.0.1', 55822) after reading no data
    closing ('127.0.0.1', 55822) after reading no data
    
    waiting for the next event
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

import select
import socket
import sys
import Queue

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setblocking(0)
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
server.bind(server_address) # Bind the socket to the port
server.listen(5) # Listen for incoming connections


inputs = [ server ] # Sockets from which we expect to read
outputs = [ ] # Sockets to which we expect to write

message_queues = {} # Outgoing message queues (socket:Queue)

while inputs:
    # Wait for at least one of the sockets to be ready for processing
    print >>sys.stderr, '\nwaiting for the next event'
    #menunggu / block
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    # Handle inputs
    for s in readable:
        if s is server:
            # A "readable" server socket is ready to accept a connection
            connection, client_address = s.accept()
            print >>sys.stderr, 'new connection from', client_address
            connection.setblocking(0)
            inputs.append(connection)

            # Give the connection a queue for data we want to send
            message_queues[connection] = Queue.Queue()

        else:
            print "else"
            data = s.recv(1024)
            if data:
                print 'data'
                # A readable client socket has data
                print >>sys.stderr, 'received "%s" from %s' % (data, s.getpeername())
                message_queues[s].put(data)
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)
            else:
                print 'data else'
                # Interpret empty result as closed connection
                print >>sys.stderr, 'closing', client_address, 'after reading no data'
                # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                
    # Handle outputs
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except Queue.Empty:
            # No messages waiting so stop checking for writability.
            print >>sys.stderr, 'output queue for', s.getpeername(), 'is empty'
            outputs.remove(s)
        else:
            print >>sys.stderr, 'sending "%s" to %s' % (next_msg, s.getpeername())
            s.send(next_msg)