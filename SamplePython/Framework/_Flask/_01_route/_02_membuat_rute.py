from flask import Flask
app =Flask(__name__)

@app.route('/')
def hal_awal():
    return "<h1>hallo world</h1>"


@app.route('/kemana')
def hal_kemana():
    return "<h1>kemana kemana kemana</h1>"


#debug samadengan true artinya server akan memunculkan kesalahan error
app.run(debug=True)