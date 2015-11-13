"""
secara default flask akan melihat ke folder 'templates' yang terletak tepat 
di dalam folder aplikasi untuk mencari ada-tidaknya template. Oleh karena itu
template harus diletakan di dalam foldes 'templates'.
flask menggunakan bantuan jinja untuk merender template
"""

from flask import Flask, render_template

app =Flask(__name__)
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


app.run()