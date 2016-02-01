"""
Template extending

Another nice thing Django has for you is template extending. What does this mean? 
It means that you can use the same parts of your HTML for different pages of your website.

Templates help when you want to use the same information/layout in more than one place.
You don't have to repeat yourself in every file. And if you want to change something, 
you don't have to do it in every template, just once!

Create base template

A base template is the most basic template that you extend on every page of your website.

Let's create a base.html file in blog/templates/blog/:

blog
└───templates
    └───blog
            base.html
            post_list.html

Then open it up and copy everything from post_list.html to base.html file, like this:

{% load staticfiles %}
<html>
    <head>
        <title>Django Girls blog</title>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
        <link href='//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    </head>
    <body>
        <div class="page-header">
            <h1><a href="/">Django Girls Blog</a></h1>
        </div>

        <div class="content container">
            <div class="row">
                <div class="col-md-8">
                {% for post in posts %}
                    <div class="post">
                        <div class="date">
                            {{ post.published_date }}
                        </div>
                        <h1><a href="">{{ post.title }}</a></h1>
                        <p>{{ post.text|linebreaks }}</p>
                    </div>
                {% endfor %}
                </div>
            </div>
        </div>
    </body>
</html>

Then in base.html, replace your whole <body> (everything between <body> and </body>) with this:

<body>
    <div class="page-header">
        <h1><a href="/">Django Girls Blog</a></h1>
    </div>
    <div class="content container">
        <div class="row">
            <div class="col-md-8">
            {% block content %}
            {% endblock %}
            </div>
        </div>
    </div>
</body>
You might notice this replaced everything from {% for post in posts %} to {% endfor %} with:

{% block content %}
{% endblock %}

But why? You just created a block! You used the template tag {% block %} to make an 
area that will have HTML inserted in it. That HTML will come from another templates that 
extends this template (base.html). We will show you how to do this in a moment.

Now save base.html, and open your blog/templates/blog/post_list.html again. 
You're going to remove everything above {% for post in posts %} and below {% endfor %}. 
When you're done the file will look like this:

{% for post in posts %}
    <div class="post">
        <div class="date">
            {{ post.published_date }}
        </div>
        <h1><a href="">{{ post.title }}</a></h1>
        <p>{{ post.text|linebreaks }}</p>
    </div>
{% endfor %}

We want to use this as part of our template for all the content blocks. 
Time to add block tags to this file!

You want your block tag to match the tag in your base.html file. You also want it 
to include all the code that belongs in your content blocks. To do that, put everything 
between {% block content %} and {% endblock content %}. Like this:


{% block content %}
    {% for post in posts %}
        <div class="post">
            <div class="date">
                {{ post.published_date }}
            </div>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}
{% endblock %}

Only one thing left. We need to connect these two templates together. This is what extending 
templates is all about! We'll do this by adding an extends tag to the beginning of the file.
Like this:

{% extends 'blog/base.html' %}

{% block content %}
    {% for post in posts %}
        <div class="post">
            <div class="date">
                {{ post.published_date }}
            </div>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}
{% endblock %}

That's it! Check if your website is still working properly :)
If you have an error TemplateDoesNotExist that says that there is no blog/base.html 
file and you have runserver running in the console, try to stop it (by pressing Ctrl+C - 
Control and C buttons together) and restart it by running a python manage.py runserver 
command.
"""