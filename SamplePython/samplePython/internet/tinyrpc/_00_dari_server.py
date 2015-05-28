from tinyrpc.protocols.jsonrpc import JSONRPCProtocol


def event_pesawat_subscribe():
    print "event-pesawat"

def data_pesawat():
    pass

methods = {"flight-event-subscribe"     :  event_pesawat_subscribe,
           "fligt-data"                 :  data_pesawat
           }
#ini diibaratkan RPC yang masuk dari client
data_dari_client = '{"jsonrpc": "2.0", "method": "flight-event-subscribe", "id": 4}'
data_dari_client_berparam = '{"params": {"id": 1}, "jsonrpc": "2.0", "method": "authenticate", "id": 1}'
"""
setelah client mengirim rpc, maka server menangkap rpc, karna client mengirim dalam bentuk string, 
maka kita kembalikan kedalam bentuk objek rpc, jadi
1. buat instance dari JSONRPCProtocol
2. ubah string menjadi objek rpc menggunakan method parse_request 
3. buat handler
4. panggil handler
5. buat variabel untuk menampung jawaban menggunakan respond
6. dan hasil akhir dalam bentuk string menggunakan serialize siap dikirim kembali
"""
ini_adalah_instance = JSONRPCProtocol() 
request = ini_adalah_instance.parse_request(data_dari_client)
ini_adalah_handler = methods[request.method]
ini_adalah_handler()
ini_respond = request.respond("Ini jawaban") #seharusnya disimpan di fungsi pemanggil cuman karna ini mah contoh biarkan saja lah
print ini_respond.serialize()

#Untuk mengakses data berparam
request_berparam = ini_adalah_instance.parse_request(data_dari_client_berparam)
print "request_berparam.method = ", request_berparam.method
print "request_berparam.kwargs['id'] = ", request_berparam.kwargs['id']