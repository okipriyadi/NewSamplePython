from flask import Flask
#memasukan __name__ dalam argumen agar halaman ini menjadi halaman root dari aplikasi flask ini
app =Flask(__name__)
#menjalankan server dengan method run()
app.run()
