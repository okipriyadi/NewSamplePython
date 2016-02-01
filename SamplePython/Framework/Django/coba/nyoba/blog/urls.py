from django.conf.urls import patterns, url
from views import archive

urlpatterns = patterns('',
                       url(r'^$', archive),
                       )