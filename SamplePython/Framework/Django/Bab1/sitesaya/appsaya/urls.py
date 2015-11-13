from django.conf.urls.defaults import *
from views import archive

urlpatterns = patterns('',url(r'^$', archive),)
