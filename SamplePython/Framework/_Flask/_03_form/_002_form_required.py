"""
There are cases where you may want to set special attributes for the input
element for example, required , which tells your browser that the given field should
not be submitted if empty. Call field as a function in order to achieve that, like so:

*Lihat di bagiian template terdapat 

{{ field.flags.required }}
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
    return render_template('_002_form_with_wtfform.html', form=form())


app.run(debug=True)