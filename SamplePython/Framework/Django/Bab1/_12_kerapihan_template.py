"""
if our site had a blog, a
photo archive, and a links page, and we wanted all these to 
be based on a common base, what we are going to do?

Experience tells you the wrong way to do this would be to copy and paste your way to
three kind-of-identical self-contained templates.The right way in Django is to create a
base template, and then extend this template to generate the other, specific templates. In
your mysite/blog/templates directory, create a template called base.html containing
the following:
==============================================================================+
<html>
<style type="text/css">
body { color: #efd; background: #453; padding: 0 5em; margin: 0 }
    h1 { padding: 2em 1em; background: #675 }
    h2 { color: #bf8; border-top: 1px dotted #fff; margin-top: 2em }
    p { margin: 1em 0 }
    </style>
<body>
<h1>mysite.example.com</h1>
{% block content %}
{% endblock %}
</body>
</html>
==============================================================================+

Not exactly valid XHTML Strict, but it’ll do.The detail to notice is the {% block ...
tag.This defines a named area that subtemplates can change.To make your blog app use
this template, change your archive.html template so it references this new base template
and its “content” block.
"""


