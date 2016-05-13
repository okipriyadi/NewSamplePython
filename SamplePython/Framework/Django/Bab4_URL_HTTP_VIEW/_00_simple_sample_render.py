#contoh 1:
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) #post_list.html harus berada di folder templates

"""
In the render function we already have parameter with request (so everything we receive from the user via the Internet) and a template file 'blog/post_list.html'. The last parameter, which looks like this: {} is a place in which we can add some things for the template to use. We need to give them names (we will stick to 'posts' right now :)). It should look like this: {'posts': posts}. Please note that the part before : is a string; you need to wrap it with quotes ''.
"""

