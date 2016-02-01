from django.contrib import admin

# Register your models here.
from models import Tweet
admin.site.register(Tweet)

def __unicode__(self):
    return self.text