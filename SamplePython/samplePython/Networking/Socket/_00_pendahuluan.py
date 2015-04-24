"""
Socket adalah mekanisme komunikasi yang memungkinkan terjadinya pertukaran data antar program 
atau proses baik dalam satu mesin maupun antar mesin. Gaya pemrograman socket sendiri 
berawal dari sistem Unix BSD yang terkenal dengan kepeloporannya pada bidang penanganan jaringan, 
sehingga sering disebut BSD Socket.

Sockets have two primary properties controlling the way they send data: 
1. the address family => controls the OSI network layer protocol used, 
2. the socket type => controls the transport layer protocol

Python supports three address families. 
1. AF_INET , is used for IPv4 Internet addressing.
2. AF_INET6 is used for IPv6 Internet addressing.
3. AF_UNIX is the address family for UNIX Domain Sockets (UDS)

The socket type is usually either :
1. SOCK_DGRAM for user datagram protocol (UDP)
2. SOCK_STREAM for transmission control protocol (TCP)
3. SOCK_RAW
4. SOCK_RDM
5. SOCK_SECPAKET

standard port/protocol:
http     = 80
https    = 443
ftp      = 21
gopher   = 70
smtp     = 25
imap     = 143
imaps    = 993
pop3     = 110
pop3s    = 995

There are five different server classes defined in SocketServer . 
1. BaseServer
   defines the API and is not intended to be instantiated and used directly.
2. TCPServer 
   uses TCP/IP sockets to communicate. 
3. UDPServer uses datagram sockets.
4. UnixStreamServer and 
5. UnixDatagramServer 
   use UNIX-domain sockets and are only available on UNIX platforms.

Ada dua golongan socket di Unix yang paling umum dipakai yaitu:
1. Socket Lokal atau AF_UNIX
   Socket Lokal adalah socket yang melakukan komunikasi dengan perantaraan sebuah file yang biasanya 
   diletakkan pada direktori /tmp atau /usr/tmp ataupun /var/tmp. Socket semacam ini digunakan umumnya 
   terbatas untuk komunikasi antar aplikasi dalam satu mesin.
2. Socket Networking atau AF_INET
   Socket Networking ditujukan untuk komunikasi antar aplikasi antar mesin dalam 
   lingkungan jaringan TCP/IP. Identifikasi socket dilakukan dengan sebuah service identifier 
   yaitu berupa nomor port TCP/IP yang dapat di sambung oleh client.

Socket Networking memiliki beberapa jenis, yang paling umum digunakan yaitu:
a. Socket Stream atau SOCK_STREAM
   Socket Stream adalah socket komunikasi full-duplex berbasis aliran (stream) data. Pada model 
   komunikasi Socket Stream, koneksi dua aplikasi harus dalam kondisi tersambung dengan benar 
   untuk dapat bertukar data. Ini dapat dianalogikan seperti komunikasi telepon. 
   Jika sambungan telepon di salah satu titik putus, maka komunikasi tidak dapat terjadi. 
   Koneksi model seperti ini akan menjamin data dapat dipertukarkan dengan baik, namun memiliki 
   kelemahan dalam hal penggunaan jalur data yang relatif besar dan tidak boleh terputus.
b. Socket Datagram atau SOCK_DGRAM
   Socket Datagram berkomunikasi dengan cara yang berbeda. Socket ini tidak membutuhkan koneksi 
   yang tersambung dengan benar untuk mengirimkan dan menerima data. Model koneksi semacam ini 
   tidak dapat menjamin data dapat dipertukarkan dengan baik, namun memiliki keunggulan dalam hal 
   penggunaan jalur data yang minimal. Socket Datagram dapat dianalogikan dengan komunikasi yang 
   terjadi pada kelas, misalnya pada saat guru melakukan broadcasting materi pelajaran untuk diterima 
   oleh setiap murid. Tidak ada yang dapat menjamin materi pelajaran dapat diterima oleh semua murid 
   dengan baik, kecuali diterapkan metoda rechecking. Rechecking ini dapat dilakukan baik oleh guru 
   maupun murid. Guru bertanya untuk memastikan jawaban dari murid benar, atau murid bertanya untuk 
   memastikan kebenaran materi yang diterimanya. Socket Datagram pun menggunakan metoda ini untuk 
   menjamin pengiriman data dapat dilakukan dengan baik.



- Socket addresses are represented as follows: A single string is used for the AF_UNIX address family.
- A pair (host, port) is used for the AF_INET address family
    where host is a string representing either a hostname in Internet domain notation like 'daring.cwi.nl' 
    or an IPv4 address like '100.50.200.5', and port is an integer
- For AF_INET6 address family, a four-tuple (host, port, flowinfo, scopeid) is used, where flowinfo and 
    scopeid represents sin6_flowinfo and sin6_scope_id member in struct sockaddr_in6 in C

Sekilas Tentang Socket, TCP Dan UDP
Pengertian socket adalah interface pada jaringan yang menjadi titik komunikasi antarmesin pada Internet Protocol, dan tentunya tanpa komunikasi ini, tidak akan ada pertukaran data dan informasi jaringan.
Socket terdiri dari elemen-elemen utama sebagai berikut:
1. Protokol.
2. Local IP.
3. Local Port.
4. Remote IP.
5. Remote Port.

Dalam komunikasi antara dua pihak, tentunya harus digunakan kesepakatan aturan dan format yang sama 
agar komunikasi dapat dimengerti. Seperti halnya dua orang yang menggunakan bahasa yang sama, 
maka bahasa di sini berfungsi sebagai protokol. Protokol yang digunakan dalam socket dapat 
menggunakan TCP ataupun UDP.

Contoh komunikasi sederhana adalah komunikasi antara komputer A dan komputer B. Baik komputer A
maupun komputer B harus memiliki identitas unik, yang direpresentasikan oleh IP masing-masing. 
Komunikasi yang terjadi melalui port, sehingga baik komputer A maupun komputer B harus memiliki 
port yang dapat diakses satu sama lain.

Pemrograman socket adalah cara untuk menggunakan komponen/API (Application Programming Interface) socket
untuk membuat sebuah aplikasi. Aplikasi socket umumnya terdiri dari dua kategori berdasarkan 
pengiriman datanya, yaitu:
a. Datagram socket (menggunakan UDP).
b. Stream socket (menggunakan TCP).

Terdapat perlakuan yang berbeda antara UDP dan TCP, walaupun sama-sama berfungsi sebagai protokol 
pertukaran data. UDP tidak memerlukan proses koneksi terlebih dahulu untuk dapat mengirimkan data, 
paket-paket data yang dikirimkan UDP bisa jadi melalui rute yang berbeda-beda, sehingga hasil yang 
diterima bisa jadi tidak berurutan.

Contohnya jika aplikasi socket pengirim mengirimkan berturut-turut pesan 1, pesan 2, dan pesan 3, 
maka aplikasi socket penerima belum tentu mendapatkan pesan yang berurutan dimulai dari pesan 1, 
pesan 2, dan terakhir pesan 3. Bisa saja pesan 2 terlebih dulu diterima, menyusul pesan-pesan yang lain,
atau berbagai kemungkinan lainnya. Bahkan, dapat terjadi pesan yang dikirimkan tidak sampai ke 
penerima karena kegagalan pengiriman paket data.

Tidak demikian halnya dengan stream socket yang menggunakan TCP. Jenis ini mengharuskan terjadinya 
koneksi terlebih dahulu, kemudian mengirimkan paket-paket data secara berurutan, penerima juga dijamin 
akan menerima data dengan urutan yang benar, dimulai dari data pertama yang dikirimkan hingga data 
terakhir. TCP dapat menangani data yang hilang, rusak, terpecah, ataupun terduplikasi.  

Dari sekilas perbedaan ini, kita dapat menarik kesimpulan bahwa aplikasi socket yang menggunakan 
TCP memerlukan pertukaran data dua arah yang valid. Sedangkan, aplikasi socket yang menggunakan 
UDP lebih memprioritaskan pada pengumpulan data.

Karena itu aplikasi socket dengan TCP sering diterapkan untuk aplikasi chat, transfer ﬁle, 
ataupun transaksi-transaksi penting. Sedangkan aplikasi socket dengan UDP cocok diterapkan untuk 
aplikasi monitoring jaringan, game online, dan aplikasi-aplikasi broadcast.

D.  Port dan Winsock
1.   Port
Salah satu elemen penting yang digunakan dalam aplikasi socket adalah port. Port merupakan sebuah 
koneksi data virtual yang digunakan aplikasi untuk bertukar data secara langsung. Terdapat banyak port 
di dalam sebuah sistem komputer dengan fungsinya masing-masing. Sebagai contoh, dalam mengirim e-mail 
digunakan service SMTP yang umumnya menggunakan port 25. Sementara service POP3 untuk menerima e-mail 
menggunakan port 110, port 80 digunakan untuk HTTP, port 443 digunakan untuk HTTPS, dan seterusnya.
Nomor-nomor port dikategorikan dalam tiga jenis sebagai berikut:
a. Well-known ports.
   Merupakan port yang telah digunakan secara internal oleh sistem Windows, misalnya port 
   untuk koneksi Internet, service FTP, dan seterusnya. Port yang telah digunakan ini adalah 
   port 0 sampai dengan port 1023.
b. Registered ports.
   Port ini dapat digunakan dalam aplikasi Anda, range-nya adalah port 1024 hingga port 49151, 
   cukup banyak port yang tersedia yang bebas Anda pilih sehingga Anda tidak perlu kuatir kekurangan 
   port untuk aplikasi Anda.
c. Dynamic/Private ports.
   Dari port 49152 sampai dengan port 65535.

Winsock
Untuk pemrograman aplikasi socket berbasis Windows, maka komponen API yang sering digunakan adalah 
Winsock (Win-dows Socket API) yang mendukung interface standar TCP/IP, yang merupakan protokol 
jaringan paling popular saat ini (contoh protokol jaringan yang lain adalah NetBIOS, IPX dari Novell,
AppleTalk dari Apple, dan sebagainya). Pengertian TCP/IP (TCP over IP) mungkin dapat menjadi 
sedikit rancu jika diartikan TCP/IP hanya mengizinkan pengiriman TCP (dan tidak UDP), padahal 
seperti yang telah kita bahas, pengiriman socket dapat melalui TCP maupun UDP. Pengertian TCP/IP di 
sini sebenarnya digunakan untuk menunjukkan teknologi jaringan/Internet, termasuk di dalamnya adalah 
UDP. Jika Anda menggunakan UDP, dapat juga disebut sebagai UDP/IP (UDP over IP), tetapi umumnya istilah 
ini jarang digunakan dan istilah TCP/IP telah mencakup, baik TCP maupun UDP.

Pada bahasa pemrograman visual seperti Visual Basic/Delphi, Anda dapat menggunakan control Winsock yang
telah disediakan untuk mengembangkan aplikasi socket. Walaupun kita akan mencontohkan aplikasi socket 
dalam environment Windows, Anda tidak perlu khawatir jika aplikasi socket yang menggunakan Winsock 
tidak dapat berkomunikasi dengan aplikasi socket berbasis Unix/Linux, karena komunikasi tetap dapat 
terjadi selama aplikasi tersebut menggunakan protokol jaringan yang sama.
Bagi Anda yang terpaksa hanya menggunakan satu komputer, dapat memanfaatkan alamat localhost atau 
127.0.0.1 yang mengizinkan dua aplikasi berjalan pada satu mesin komputer dan berkomunikasi satu sama 
lain.

Tools Tambahan
Aplikasi socket merupakan aplikasi jaringan dan jika Anda mendalami seluk-beluk jaringan, tentu akan 
familiar dengan tools tambahan yang umumnya digunakan dalam jaringan. Tools ini kemungkinan dapat 
berguna untuk diimplementasikan ke dalam aplikasi socket Anda.

Tools yang dimaksud, antara lain:
a. Ping.
   Ping digunakan untuk memeriksa keberadaan remote host dengan jalan mengirimkan sinyal kepada 
   remote host. Keberadaan remote host dapat ditentukan dengan melihat response yang diterima. 
   Ping juga dapat digunakan untuk mengukur kecepatan transfer data. Salah satu contoh penggunaan 
   ping dalam aplikasi socket adalah memeriksa server yang tersedia sebelum mengirimkan data 
   (dengan asumsi tersedia lebih dari 1 server).
b. Telnet.
   Telnet merupakan singkatan dari TELecommunication NET-work. Umumnya istilah telnet saat ini 
   merujuk pada aplikasi telnet client yang tersedia pada kebanyakan operating sys-tem. Telnet 
   mengizinkan Anda mengakses remote host dan menggunakan service-nya. Sebagai contoh, Anda dapat 
   mengirimkan e-mail melalui telnet yang menggunakan port 25 (service SMTP) pada remote host tertentu. 
   Jika Anda telah masuk ke dalam environment telnet, command line yang digunakan adalah command 
   berbasis Unix/Linux. Aplikasi socket dapat dimodiﬁkasi bekerja seperti telnet dengan mengakses 
   remote host dan port tertentu. Di dalam aplikasi socket, Anda dapat mengambil dan mengolah response 
   yang didapat dari remote host.
c. Netstat.
   Netstat menampilkan status jaringan yang terjadi. Dapat menampilkan port yang sedang terkoneksi, 
   atau dalam kondisi menunggu/listening, juga menampilkan protokol yang digunakan, apakah TCP atau 
   UDP. Dengan Netstat, Anda dapat mengetahui koneksi jaringan yang terjadi, hal ini dapat dimanfaatkan
   di dalam aplikasi socket, misalnya untuk melihat port yang sedang aktif dan digunakan.

Ada kalanya Anda perlu menjalankan tools jaringan yang telah disebutkan di atas melalui aplikasi Anda. 
Untuk keperluan ini, Anda dapat menggunakan shell command yang disediakan oleh bahasa pemrograman yang 
Anda gunakan.
Misalnya pada Visual Basic, dapat digunakan perintah Shell diikuti parameter yang diperlukan.
Jika ingin mengolah response yang dihasilkan oleh tools tertentu, Anda dapat menuliskan hasilnya 
pada sebuah ﬁle teks, contohnya jika Anda menjalankan perintah netstat –an > hasil.txt pada 
Command Prompt Windows, maka informasi mengenai koneksi yang aktif akan tersimpan dalam ﬁle 
hasil.txt, di mana Anda dapat mengolah ﬁle hasil.txt tersebut lebih lanjut di dalam aplikasi Anda.

Socket adalah sebuah cara untuk berkomunikasi dengan program atau node lain menggunakan file deskriptor. Di UNIX (dimana socket diciptakan) kita sering mendengar slogan: “everything is a file”, jadi untuk berkomunikasi dengan program atau node lain semudah kita membaca dan menulis file deskriptor. Antarmuka socket dan file adalah mirip, jika pada file kita membukanya dengan open() sedangkan pada socket kita manggunakan socket(). Pada file deskriptor yang menjadi tujuan adalah sebuah file, sedangkan pada socket adalah komputer atau node lain. Intinya ketika kita telah terhubung dengan socket(), maka antarmukanya sama saja dengan sebuah file. Sebuah abstraksi perangkat lunak yang digunakan sebagai suatu “terminal” dari suatu hubungan antara dua mesin atau proses yang saling berinterkoneksi
Penggunaan socket programming memungkinkan adanya komunikasi antara client dan server. Salah satu contoh sederhana penggunaan socket programming adalah pembuatan program untuk chatting. Program tersebut sebenarnya merupakan bentuk aplikasi berupa komunikasi antara client dan server. Ketika seorang user (client) melakukan koneksi ke chat server, program akan membuka koneksi ke port yang diberikan, sehingga server perlu membuka socket pada port tersebut dan “mendengarkan” koneksi yang datang. Socket sendiri merupakan gabungan antara host-adress dan port adress. Dalam hal ini socket digunakan untuk komunikasi antara client dan server.
Socket merupakan fasilitas IPC (Inter Proses Communication) untuk aplikasi jaringan. Agar suatu socket dapat berkomunikasi dengan socket lainnya, maka socket butuh diberi suatu alamat unik sebagai identifikasi. Alamat socket terdiri atas Alamat IP dan Nomer Port. Contoh alamat socket adalah 192.168.29.30: 3000, dimana nomer 3000 adalah nomer portnya. Alamat IP dapat menggunakan alamat Jaringan Lokal (LAN) maupun alamat internet. Jadi socket dapat digunakan untuk IPC pada LAN maupun Internet.

Obyek socket pada sisi client dan server berbeda sedikit. Pada sisi aplikasi server, suatu socket 
server dibentuk dan melakukan operasi listen/menunggu. Operasi ini pada intinya menunggu 
permintaan koneksi dari sisi client. Sedangkan pada sisi client, dibentuk suatu socket biasa.

Pada saat socket client, informasi alamat socket server dilewatkan sebagai argumen dan 
socket client akan otomatis mencoba meminta koneksi ke socket server. Pada saat permintaan koneksi 
client sampai pada server, maka server akan membuat suatu socket biasa. Socket ini yang nantinya 
akan berkomunikasi dengan socket pada sisi client. Setelah itu socket server dapat kembali 
melakukan listen untuk menunggu permintaan koneksi dari client lainnya. Langkah ini umumnya hanya 
dilakukan jika aplikasi server mengimplementasikan multithreading.

Setelah tercipta koneksi antara client dan server, maka keduanya dapat saling bertukar pesan. 
Salah satu atau keduanya kemudian dapat mengakhiri komunikasi dengan menutup socket.
Untuk protokol UDP, perbedaanya adalah socket di sisi server sama dengan socket di sisi client, 
dan tidak ada operasi listen pada sisi server. Kemudian saat paket data dikirimkan, alamat socket 
penerima harus disertakan sebagai argumen.


"""
