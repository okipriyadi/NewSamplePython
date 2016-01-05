"""
Construct adalah python library untuk construction dan deconstruction struktur data secara dekaratif. 
Dalam konteks ini, konstruksi(building), mengacu pada proses konversi (serialisasi) objek program 
menjadi representasi biner. Dekonstruksi (parsing) mengacu pada proses kebalikan dari konversi (deserializing)
data biner menjadi objek program (objek yang tersusun)

Menjadi deklaratif berarti bahwa kode yang kita buat mendefinisikan struktur data, 
Construct dapat bekerja secara lancar dengan bit dan/atau juga byte-level data granularity dan berbagai 
macam byte-ordering.

Menggunakan deklaratif memiliki banyak manfaat. Sebagai contoh, kode yang sama yang dapat memparse, 
juga dapat mem-build.  Debugging and testing menjadi lebih sederhana , menciptakan constructs baru 
menjadi mudah, dan masih banyak lagi manfaat lainnya. 


Contoh berikut menunjukkan bagaimana TCP / IP protokol stack dapat didefinisikan menggunakan construct; 
beberapa kode dihilangkan agar code menjadi singkat dan sederhana. 
Juga mencatat bahwa kode berikut hanya kode python yang menciptakan object.
"""
from construct import Struct, Bytes, UBInt16, Enum, EmbeddedBitStruct, Const, Nibble, BitStruct, Bits, Flag, Padding

#First, the ethernet header (layer 2):
ethernet = Struct("ethernet_header",
    Bytes("destination", 6),
    Bytes("source", 6),
    Enum(UBInt16("type"),
        IPv4=0x0800,
        ARP=0x0806,
        RARP=0x8035,
        X25=0x0805,
        IPX=0x8137,
        IPv6=0x86DD,
    ),
 )

#Next, the IP header (layer 3):
ip = Struct("ip_header",
    EmbeddedBitStruct(
        Const(Nibble("version"), 4),
        Nibble("header_length"),
    ),
    BitStruct("tos",
        Bits("precedence", 3),
        Flag("minimize_delay"),
        Flag("high_throuput"),
        Flag("high_reliability"),
        Flag("minimize_cost"),
        Padding(1),
    ),
    UBInt16("total_length"),
    # ...
 )