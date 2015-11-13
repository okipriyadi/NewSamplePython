"""
untuk form gunakan bantuan tools flask-WTF

pip install flask-wtf


secara default, Flask-WTF memproteksi semua form dari serangan Cross-Site Request 
Forgery (CSRF) attacks. A CSRF attack occurs when a malicious website sends 
requests to a different website on which the victim is logged in.

Untuk mengimplementasikan CSRF protection, Flask-WTF perlu mengkonfigurasi en
cryption key. Flask-WTF menggunaan key ini untuk mengenerate encrypted tokens 
yang digunakan untuk memverifikasi dan mengauthentifikasi.


Field type              Description
StringField             Text field
TextAreaField           Multiple-line text field
PasswordField           Password text field
HiddenField             Hidden text field
DateField               Text field that accepts a datetime.date value in a given format
DateTimeField           Text field that accepts a datetime.datetime value in a given format
IntegerField            Text field that accepts an integer value
DecimalField            Text field that accepts a decimal.Decimal value
FloatField              Text field that accepts a floating-point value
BooleanField            Checkbox with True and False values
RadioField              List of radio buttons
SelectField             Drop-down list of choices
SelectMultipleField     Drop-down list of choices with multiple selection
FileField               File upload field
SubmitField             Form submission button
FormField               Embed a form as a field in a container form
FieldList               List of fields of a given type


WTF-FALIDATOR
Validator             Description
Email                 Validates an email address
EqualTo               Compares the values of two fields; useful when requesting a password to be entered twice for confirmation
IPAddress             Validates an IPv4 network address
Length                Validates the length of the string entered
NumberRange           Validates that the value entered is within a numeric range
Optional              Allows empty input on the field, skipping additional validators
Required              Validates that the field contains data
Regexp                Validates the input against a regular expression
URL                   Validates a URL
AnyOf                 Validates that the input is one of a list of possible values
NoneOf                Validates that the input is none of a list of possible values
"""
from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required



app = Flask(__name__)
#method .config adalah dictionary yang digunakan untuk menyimpan konfigurasi
app.config['SECRET_KEY'] = 'hard to guess string'


"""
Ketika menggunakan WTF setiap form direpresentasikan sebagai sebuah class yg merupakan keturunan dari kelas form. 
kelas tersebut mendefinisikan  list fields dari form tersebut, 
yang direpresentasikan sebagai sebuah object. setiap objek field dapat memiliki satu atau lebih validator; 
validators adalah fungsi yang mengecek apakah inputan dari user valid.
"""

class NameForm(Form):
    #The Required() validator ensures that the field is not submitted empty
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
    
form = NameForm
@app.route('/formulir')
def iniform():
    #istance dari kelas NameForm harus callable diberi kurungbuka/tutup
    return render_template('formulir.html', form=form())


app.run(debug=True)