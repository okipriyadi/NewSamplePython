from base64 import b64encode, b64decode

teks = "ini kode"


payload = b64encode(teks)
print teks, "setelah di encode menjadi :", payload

_decode = b64decode(payload)
print payload, "setelah di decode menjadi :", _decode
