"""
A page, from Django's perspective, has three typical components:
1. A template that displays information passed to it (in a Python-dictionary-like object called a Context )
2. A view function that fetches information to be displayed, typically from a database
3. A URL pattern that matches an incoming request with your view function, optionally passing parameters to the view as well

we'll tackle these three in that order. In a sense this is building from the inside out.
when Django processes a request, it starts with the URL patterns, then calls the view, and
then returns the data rendered into a template.

We’ll tackle these three in that order. In a sense this is building from the inside out—
when Django processes a request, it starts with the URL patterns, then calls the view, and
then returns the data rendered into a template.


Creating a Template
Django’s template language is easy enough to read that we can jump right in to example
code.This is a simple template for displaying a single blog post:

<h2>{{ post.title }}</h2>
<p>{{ post.timestamp }}</p>
<p>{{ post.body }}</p>

It’s just HTML (though Django templates can be used for any kind of textual output)
plus special template tags in curly braces.These are variable tags, which display data
passed to the template. Inside a variable tag, you can use Python-style dot-notation to
access attributes of the objects you pass to your template. 

For example, this template assumes you have passed it a BlogPost object called “post.”The three lines of the template
fetch the BlogPost object’s title , timestamp , and body fields, respectively
Let’s enhance the template a bit so it can be used to display multiple blog posts, using
Django’s for template tag.

{% for post in posts %}
<h2>{{ post.title }}</h2>
<p>{{ post.timestamp }}</p>
<p>{{ post.body }}</p>
{% endfor %}

The original three lines are unchanged; we’ve simply added a block tag called for that
renders a template section once for each of a sequence of items.The syntax is deliberately
similar to Python’s loop syntax. Note that unlike variable tags, block tags are enclosed in
{% ... %} pairs.

Save this simple five-line template in a file called archive.html , and put that file in a
directory called templates inside your blog app directory.That is, the path to your tem-
plate file should be:

sitesaya/appsaya/templates/archive.html

The name of the template itself is ARBITRARY(we could have called it foo.html ), but the
directory name is MANDATORY By default, when searching for templates, Django
looks for a templates directory inside each of your installed applications.
"""


