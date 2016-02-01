"""
Django templates

Time to display some data! Django gives us some helpful built-in template tags for that.

What are template tags?

You see, in HTML, you can't really write Python code, because browsers don't understand it.
They only know HTML. We know that HTML is rather static, while Python is much more dynamic.

Django template tags allow us to transfer Python-like things into HTML, so you can build 
dynamic websites faster and easier. Yikes!

Display post list template

In the previous chapter we gave our template a list of posts in the posts variable.
Now we will display it in HTML.To print a variable in Django templates, 
we use double curly brackets with the variable's name inside, like this:

{{ posts }}
Try this in your blog/templates/blog/post_list.html template. 
Replace everything from the second <div> to the third </div> with {{ posts }}. 
Save the file, and refresh the page to see the results:


[<Post: My second post>, <Post: My first post>]
This means that Django understands it as a list of objects. Remember from Introduction to Python how we can display lists? Yes, with for loops! In a Django template you do them like this:

{% for post in posts %}
    {{ post }}
{% endfor %}
Try this in your template.


It works! But we want them to be displayed like the static posts we created earlier 
in the Introduction to HTML chapter. You can mix HTML and template tags. 
Our body will look like this:
=================================================
<div>
    <h1><a href="/">Django Girls Blog</a></h1>
</div>

{% for post in posts %}
    <div>
        <p>published: {{ post.published_date }}</p>
        <h1><a href="">{{ post.title }}</a></h1>
        <p>{{ post.text|linebreaks }}</p>
    </div>
{% endfor %}
=================================================
Everything you put between {% for %} and {% endfor %} will be repeated for each object 
in the list. Refresh your page:

Figure 13.3

Have you noticed that we used a slightly different notation this time 
{{ post.title }} or {{ post.text }}? We are accessing data in each of the fields 
defined in our Post model. Also the |linebreaks is piping the posts' text through a filter 
to convert line-breaks into paragraphs.

One more thing

It'd be good to see if your website will still be working on the public Internet, right? 
Let's try deploying to PythonAnywhere again. Here's a recap of the steps...

First, push your code to Github
$ git status
[...]
$ git add -A .
$ git status
[...]
$ git commit -m "Modified templates to display posts from database."
[...]
$ git push
Then, log back in to PythonAnywhere and go to your Bash console (or start a new one), and run:
$ cd my-first-blog
$ git pull
[...]
Finally, hop on over to the Web tab and hit Reload on your web app. 
Your update should be live!
Congrats! Now go ahead and try adding a new post in your Django admin 
(remember to add published_date!) Make sure you are in the Django admin for your 
pythonanywhere site, https://www.yourname.pythonanywhere.com/admin. 
Then refresh your page to see if the post appears there.

Works like a charm? We're proud! Step away from your computer for a bit, 
you have earned a break. :)

"""