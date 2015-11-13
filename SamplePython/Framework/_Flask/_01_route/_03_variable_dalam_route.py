from flask import Flask

app =Flask(__name__)

@app.route('/')
def hal_awal():
    return "<h1>hallo world</h1>"


@app.route('/kemana')
def hal_kemana():
    return "<h1>kemana kemana kemana</h1>"

#jangan lupa memasukan variabel ke dalam parameter fungsi
@app.route('/variabel/<nama>')
def say_hai(nama):
    return "<h1>Hai %s</h1>"%nama

#debug samadengan true artinya server akan otomatis restart jika ada perubahan
app.run(debug=True)