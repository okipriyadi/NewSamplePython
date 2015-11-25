"""
WTForms is a standalone robust form handling library that allows you to generate HTML 
forms from form-like classes,
implement fields and form validation, and include cross-source forgery protection
(a nasty vulnerability that crackers may try to exploit in your Web applications).
We certainly don't want that!

Contoh ini hanya untuk merender templatenya saja, tombol submit dan penangannya masih belum dibahas disini jadi tombol submit belum berjalan
"""
from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms import Form, StringField, PasswordField, SubmitField

app = Flask(__name__)
#method .config adalah dictionary yang digunakan untuk menyimpan konfigurasi
app.config['SECRET_KEY'] = 'hard to guess string'


class LoginForm(Form):
    username = StringField(u'Username:')
    passwd = PasswordField(u'Password:')
    submit = SubmitField('Submit')
    
    
form = LoginForm

@app.route('/')
def iniform():

    #istance dari kelas NameForm harus callable diberi kurungbuka/tutup
    return render_template('_001_form_with_wtfform.html', form=form())


app.run(debug=True)