from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
"""
membuat rpc
1. buat instance dari JSONRPCProtocol
2. tambahkan method create_request
"""

ini_instance = JSONRPCProtocol()
request = ini_instance.create_request('flight-event-subscribe')#bisa juga menambahkan parameter misal request = self.rpc.create_request('authenticate', {'id' : self.client_id})

#contoh request dengan param
request4 = ini_instance.create_request('flight-event-subscribe', {'id' : '1'})

"""
melihat uniq id yg dibuat secara otomatis oleh rpc
"""
request2 = ini_instance.create_request('flight-event-subscribe2',)
request3 = ini_instance.create_request('flight-event-subscribe3')
print request.unique_id
print request2.unique_id
print request3.unique_id
print request4.unique_id

"""
Hasil Akhir yang siap dikirim
"""
print "type request",  type(request)
print "type request.serialize =", type(request.serialize())
print request.serialize()

#lihat bedanya dengan yang ada paramnya
print "\ndengan param"
print request4.serialize()
"""
Hasil balik dari SERVER
kita asumsikan server telah mengirim data yang diminta
maka tahap selanjutnya
1. buat data dari server menjadi object rpc menggunakan parse_reply
2. hasilnya bs d dapat dgn method .result

"""

data_dari_server = '{"jsonrpc": "2.0", "id": 1, "result": "ini_jawaban"}'
response = ini_instance.parse_reply(data_dari_server)
print "\n=====================\nresult reply=", response.result
#ini_handler = methods[request.method]