from flask import Flask, render_template, request
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
    
@app.route('/formulir')
def iniform():
    form = NameForm()
    return render_template('formulir.html', form=form)

#argumen 'method' untuk menangani method, dalam hal ini bisa post maupun get
@app.route('/tampi', methods=['GET', 'POST'])
def tampi():
    name = None
    form = NameForm()
    if request.method =='POST':
        name = form.name.data
        form.name.data = ''
    return render_template('tampi.html', form=form, name=name)

app.run(debug=True)