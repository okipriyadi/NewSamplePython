"""
from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


app =Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
"""

from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

"""
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    #if request.method == 'POST':
    print form.validate_on_submit()
    if form.validate_on_submit():
        old_name = session.get('name')
        print old_name
        print form.name.data
        if old_name is not None and old_name != form.name.data:
            print "ehat te"
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        #return redirect(url_for('index'))
    return render_template('tampi3.html', form=form, name=session.get('name'))

"""
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('tampi3.html', form=form, name=session.get('name'))
app.run(debug=True)