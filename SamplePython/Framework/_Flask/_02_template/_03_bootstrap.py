"""
install bootstap untuk tampilan yang disediakan TP3 yaitu twitter

pip install flask-bootstr
"""

from flask import Flask, render_template
#import modul
from flask.ext.bootstrap import Bootstrap

app =Flask(__name__)
#instansiasi bootstrap denga cara memasukan app sebagai argumen
bootstrap = Bootstrap(app)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('bootstrap.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

app.run()