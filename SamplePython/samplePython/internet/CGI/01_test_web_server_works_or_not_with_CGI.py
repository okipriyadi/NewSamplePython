"""
The Python standard library includes some modules that are helpful for creating plain 
CGI programs:

1. cgi      : Handling of user input in CGI scripts
2. cgitb    : Displays nice tracebacks when errors happen in CGI applications, 
instead of presenting a "500 Internal Server Error"     message

The Python wiki features a page on CGI scripts with some additional information about 
CGI in Python.

Depending on your web server configuration, you may need to save this code with 
a .py or .cgi extension. Additionally, this file may also need to be in a cgi-bin folder, 
for security reasons.

You might wonder what the cgitb line is about. This line makes it possible to display 
a nice traceback instead of just crashing and displaying an "Internal Server Error" 
in the user's browser. This is useful for debugging, but it might risk exposing some 
confidential data to the user. You should not use cgitb in production code for this reason. 
You should always catch exceptions, and display proper error pages 
end-users don't like to see nondescript "Internal Server Errors" in their browsers.
"""

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()

print "Content-Type: text/plain;charset=utf-8"

print "Hello World!"


"""
If you don't have your own web server, this does not apply to you. 
You can check whether it works as-is, and if not you will need to talk to the 
administrator of your web server. If it is a big host, you can try filing a ticket 
asking for Python support.

If you are your own administrator or want to set up CGI for testing purposes on your 
own computers, you have to configure it by yourself. There is no single way to configure CGI,
as there are many web servers with different configuration options. Currently the most 
widely used free web server is Apache HTTPd, or Apache for short. Apache can be easily 
installed on nearly every system using the system's package management tool. 
lighttpd is another alternative and is said to have better performance. 
On many systems this server can also be installed using the package management tool, 
so manually compiling the web server may not be needed.

On Apache you can take a look at the Dynamic Content with CGI tutorial, 
where everything is described. Most of the time it is enough just to set +ExecCGI. 
The tutorial also describes the most common gotchas that might arise.
On lighttpd you need to use the CGI module, which can be configured in a 
straightforward way. It boils down to setting cgi.assign properly.
"""
