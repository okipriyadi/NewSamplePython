from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
NOTE :
don't use it again from django.conf.urls import patterns
You should use a list because patterns() is deprecated since version 1.8, and will be removed in 1.10:
sebagai gantinya pake
===========================================================+
from django.conf.urls import url    
    urlpatterns =  [
            url(r'^$', archive),
        ]
===========================================================+
