"""
There is a special type of response called a redirect. This response does not include a
page document; it just gives the browser a new URL from which to load a new page.
Redirects are commonly used with web forms, as you will learn in Chapter 4.
A redirect is typically indicated with a 302 response status code and the URL to redirect
to given in a Location header. A redirect response can be generated using a three-value
return, or also with a Response object, but given its frequent use, Flask provides a
redirect() helper function that creates this response:
from flask import redirect
"""
from flask import Flask
#jangan lupa import redirect
from flask import redirect
app =Flask(__name__)

@app.route('/')
def hal_awal():
    return "<h1>hallo world</h1>"


@app.route('/kemana')
def hal_kemana():
    return "<h1>kemana kemana kemana</h1>"


@app.route('/variabel/<nama>')
def say_hai(nama):
    return "<h1>Hai %s</h1>"%nama


@app.route('/terjemahan')
def terjemahan():
    return redirect('https://www.google.co.id')


app.run(debug=True)