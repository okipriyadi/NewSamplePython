"""
A view in Django terminology is a regular Python function that responds to a page
request by generating the corresponding page. To write our first Django view for the
main page, we first need to create a Django application inside our project. You can
think of an application as a container for views and data models. To create it, issue
the following command within our django_mytweets folder:
==========================================================================
$ python manage.py startapp tweets
==========================================================================
The syntax of application creation is very similar to that of project creation. We used
the startapp command as the first parameter of the python manage.py command,
and provided tweets as the name of our application.

After running this command, Django will create a folder named tweets inside the
project folder with these three files:
•     __init__.py : This file tells Python that tweets is a Python package
•     views.py : This file will contain our views
•     models.py : This file will contain our data models
.     etc

Now let's create the main page view. We will first create a template folder inside the
project to keep all the HTML files:
===========================
$mkdir templates
===========================
Now create a base HTML file inside it named base.html with the following content:
============================================================================
{% load staticfiles %}
<html>
    <head>
        <link href="{% static 'bootstrap/css/bootstrap.min.css' %}" rel="stylesheet" media="screen" />">
    </head>
    <body>
        {% block content %}
            <h1 class="text-info">">HELLO DJANGO!</h1>
        {% endblock %}
        <script src="{% static 'bootstrap/js/bootstrap.min.js' %}"></script>
    </body>
</html>
============================================================================
Our directory structure will look something like this now (use the tree command if
you are on Linux OS):
mytweets/
|-- manage.py
|-- mytweets
| |-- __init__.py
| |-- __init__.pyc
| |-- settings.py
| |-- settings.pyc
| |-- urls.py
| |-- urls.pyc
| |-- wsgi.py
| `-- wsgi.pyc
|-- static
| |-- css
| | |-- bootstrap.css
| | |-- bootstrap.css.map
| | |-- bootstrap.min.css
| | |-- bootstrap-theme.css
| | |-- bootstrap-theme.css.map
| | `-- bootstrap-theme.min.css
| |-- fonts
| | |-- glyphicons-halflings-regular.eot
| | |-- glyphicons-halflings-regular.svg
| | |-- glyphicons-halflings-regular.ttf
| | `-- glyphicons-halflings-regular.woff
| `-- js
| |-- bootstrap.js
| `-- bootstrap.min.js
|-- templates
| `-- base.html
`-- tweets
    |-- admin.py
    |-- __init__.py
    |-- models.py
    |-- tests.py
    `-- views.py


Introduction to class-based views
Class-based views are the new way of defining views in Django. They do not replace
function-based views. They are just an ALTERNATIVE way to implement views as Python
objects instead of functions. There are two advantages they have over function-
based views. With a class-based view, different HTTP requests can be mapped to a
different function, as opposed to a function-based view where the branching takes
place based on the request.method parameter. Object-oriented techniques can be
used to reuse the code component, such as mixins (multiple inheritance).
Although we will be using class-based views for our project, to understand the exact
difference between the two, here we will present the code for both.
We will have to update the url.py file of our project so that the base.html file will
be served if the user requests the website.

Function-based view:
Update the view.py file as follows:
=======================================================+
from django.http import HttpResponse
def index(request):
    if request.method == 'GET':
        return HttpResponse('I am called from a get Request')
    elif request.method == 'POST':
        return HttpResponse('I am called from a post Request')
=======================================================+

Update the urls.py file as follows:
=======================================================+
from django.conf.urls import patterns, include, url
from django.contrib import admin
from tweets import views

admin.autodiscover()
urlpatterns = patterns('', 
                       url(r'^$', views.index, name='index'), 
                       url(r'^admin/', include(admin.site.urls)),)
=======================================================+
Run the development server by using the following command:
$python manage.py runserver
We will see a response saying I am called from a get Request.

Class-based view:
Update the views.py file as follows:
=======================================================+
from django.http import HttpResponse
from django.views.generic import View
class Index(ViewV iew):
    def get(self, request):
        return HttpResponse('I am called from a get Request')
    
    def post(self, request):
    return HttpResponse('I am called from a post Request')
=======================================================+
urls.py
=======================================================+
from django.conf.urls import patterns, include, url
from django.contrib import admin
from tweets.views import Index
admin.autodiscover()
=======================================================+

This will also generate the same result on the browser after the development server is
hit. We will be using class-based views throughout the project.
What we have rendered is just a string, which was kind of simple. We have created a
base.html file in our template folder and will now move ahead with our class-based
view and render our base.html file.
In Django, there is more than one way to render our page. We can render our
page using any of these three functions: render() , render_to_response() , or
direct_to_template() . However, let us first see what the difference between
them is and which one we should be using:

•   render_to_response(template[, dictionary][, context_instance]
    [, mimetype]) : The render_to_response command is the standard render
    function, and to use RequestContext , we will have to specify 
    context_instance=RequestContext(request) .
•   render(request, template[, dictionary][, context_instance][,content_type][, status][, current_app]). 
    This is the new shortcut for the render_to_response command and is available from version 1.3 of
    Django. This will automatically use RequestContext .
•   direct_to_template() : This is a generic view. It automatically uses RequestContext and all its 
    context_processor parameters.

However, the direct_to_template command should be avoided as function-based
generic views are deprecated.

We will choose the second one, the render() function, for rendering our
base.html template.

The next step is the inclusion of the template folder in our Django application
(the template folder we have created with the base file named base.html ). To
include the template, we will update the settings.py file in the following manner:

========================================================
TEMPLATE_DIRS = ( BASE_DIR + '/templates/' )
TEMPLATE_LOADERS = (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    )    
========================================================
This defines the template directory and initializes the basic TEMPLATE_LOADER
parameters.

and edit view.py
========================================================
from django.views.generic import View
from django.shortcuts import render
class Index(View):
    def get(self, request):
        return render(request, 'base.html', params)
========================================================


as you may have noticed, we haven't passed any variables to the template, which
is what roughly differentiates static pages and dynamic pages. Let's get ahead and
do that too. All we need is some changes in the views.py and base.html files,
as follows:
•     Changes in the views.py file:
========================================================
from django.views.generic import View
from django.shortcuts import render
class Index(View):
    def get(self, request):
        params = {}
        params["name"] = "Django"
        return render(request, 'base.html', params)
========================================================
•     Changes in the base.html file
========================================================
{% load staticfiles %}
<html>
<head>
    <link href="{% static 'bootstrap/css/bootstrap.min.css' %}", rel="stylesheet" media="screen">
</head>
<body>
    {% block content %}
        <h1>Hello {{name}}!</h1>
    {% endblock %}
    <script src="{% static 'bootstrap/js/bootstrap.min.js' %}"></script>
</body>
</html>
========================================================
We can see how simple it is. All we did is just create a map (called dictionary in
Python) and assigned the name property to it as Django and added it in the render()
function as a new parameter. It gets rendered to the base of the HTML and is easily
called {{name}} . When it is rendered, it replaces itself with Django.

"""
