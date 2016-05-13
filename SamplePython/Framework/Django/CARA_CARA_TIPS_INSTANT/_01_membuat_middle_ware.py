"""
First: The path structure
============================
If you don't have it you need to create the middleware folder within your project following the structure:

The folder middleware should be placed in the same folder as settings.py, urls,

Important: Don't forget to create the __init__.py empty file inside the middleware folder so your app recognize this folder

Second: Create the middleware
=============================
Now we should create a file for our custom middleware, in this example let's supose we want a middleware that filter the users 
based on their IP, we create a file called filter_ip_middleware.py inside the middleware folder with this code:
"""
class FilterIPMiddleware(object):
    # Check if client IP is allowed
    def process_request(self, request):
        allowed_ips = ['192.168.1.1', '123.123.123.123', ] # Authorized ip's
        ip = request.META.get('REMOTE_ADDR') # Get client IP
        if ip not in allowed_ips:
            raise Http403 # If user is not allowed raise Error

        # If IP is allowed we don't do anything
        return None
"""
Third: Add the middleware in our 'settings.py'
=============================================
We need to look for the MIDDLEWARE_CLASSES inside the settings.py and there we need to add our 
middleware (Add it in the last position). It should be like:
"""
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
     # Above are django standard middlewares

     # Now we add here our custom middleware
     'yourapp.middleware.filter_ip_middleware.FilterIPMiddleware'
     )
"""
    Done ! Now every request from every client will call your custom middleware and process your custom code !
"""