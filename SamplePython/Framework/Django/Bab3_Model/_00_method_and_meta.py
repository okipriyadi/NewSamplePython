from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
"""
def publish(self):? It is exactly the publish method we were talking about before. def means that this is a function/method and publish is the name of the method. You can change the name of the method, if you want. 

There is an example of that in the __str__ method. In this scenario, when we call __str__() we will get a text (string) with a Post title.

"""
