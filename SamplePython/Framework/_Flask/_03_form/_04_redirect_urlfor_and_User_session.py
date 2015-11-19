"""
The last version of hello.py has a usability problem. If you enter your name and submit
it and then click the refresh button on your browser, you will likely get an obscure
warning that asks for confirmation before submitting the form again. This happens
because browsers repeat the last request they have sent when they are asked to refresh
the page. When the last request sent is a POST request with form data, a refresh would
cause a duplicate form submission, which in almost all cases is not the desired action.
Many users do not understand the warning from the browser. For this reason, it is
considered good practice for web applications to never leave a POST request as a last
request sent by the browser.
This practice can be achieved by responding to POST requests with a redirect instead of
a normal response. A redirect is a special type of response that has a URL instead of a
string with HTML code. When the browser receives this response, it issues a GET request
for the redirect URL, and that is the page that is displayed. The page may take a few
more milliseconds to load because of the second request that has to be sent to the server,
but other than that, the user will not see any difference. Now the last request is a GET ,
so the refresh command works as expected. This trick is known as the Post/
Redirect/Get pattern.
But this approach brings a second problem. When the application handles the POST
request, it has access to the name entered by the user in form.name.data , but as soon
as that request ends the form data is lost. Because the POST request is handled with a
redirect, the application needs to store the name so that the redirected request can have
it and use it to build the actual response.
Applications can "remember" things from one request to the next by storing them in
the user session, private storage that is available to each connected client. The user session
was introduced in Chapter 2 as one of the variables associated with the request context.
It's called session and is accessed like a standard Python dictionary.
By default, user sessions are stored in client-side cookies that are
cryptographically signed using the configured SECRET_KEY. Any tam-
pering with the cookie content would render the signature invalid,
thus invalidating the session.
Example 4-5 shows a new version of the index() view function that implements redi-
rects and user sessions.
"""


from flask import Flask, request, render_template, session, redirect, url_for
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


app =Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/tampi', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if request.method == 'POST':
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('tampi.html', form=form, name=session.get('name'))

app.run(debug=True)


"""
In the previous version of the application, a local name variable was used to store the
name entered by the user in the form. That variable is now placed in the user session as
session['name'] so that it is remembered beyond the request.

In the previous version of the application, a local name variable was used to store the
name entered by the user in the form. That variable is now placed in the user session as
session['name'] so that it is remembered beyond the request.
Requests that come with valid form data will now end with a call to redirect() , a helper
function that generates the HTTP redirect response. The redirect() function takes
the URL to redirect to as an argument. The redirect URL used in this case is the root
URL, so the response could have been written more concisely as redirect('/') , but
instead Flask's URL generator function url_for() is used. The use of url_for() to
generate URLs is encouraged because this function generates URLs using the URL map,
so URLs are guaranteed to be compatible with defined routes and any changes made to
route names will be automatically available when using this function.
The first and only required argument to url_for() is the endpoint name, the internal
name each route has. By default, the endpoint of a route is the name of the view function
attached to it. In this example, the view function that handles the root URL is
index() , so the name given to url_for() is index .

The last change is in the render_template() function, which now obtains the name
argument directly from the session using session.get('name'). As with regular dic-
tionaries, using get() to request a dictionary key avoids an exception for keys that aren't
found, because get() returns a default value of None for a missing key.
"""