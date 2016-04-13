from django.conf.urls import patterns, url, include
from appsaya.views import archive

urlpatterns = patterns('',
			url(r'^$', archive),
			)


