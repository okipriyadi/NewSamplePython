from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods=['get', 'post'])
def login_view():
    # the methods that handle requests are called views, in flask
    msg = ''
    # form is a dictionary like attribute that holds the form data
    if request.method == 'POST':
        username = request.form["username"]
        passwd = request.form["passwd"]
        # static useless validation
        if username == 'you' and passwd == 'flask':
            msg = 'Username and password are correct'
        else:
            msg = 'Username or password are incorrect'
    return render_template('form.html', message=msg)

if __name__=='__main__':
    app.run()