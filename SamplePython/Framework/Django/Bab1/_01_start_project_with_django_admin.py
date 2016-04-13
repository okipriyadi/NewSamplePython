"""
The easiest way to organize your Django code when you are starting out is to use what
Django calls a project:A directory of files that constitute, usually, a single Web site. Django
comes with a utility called django-admin.py to streamline tasks such as the creation of
these project directories. On Unix, it has a default installation into the /usr/bin directory,
and if you’re on Win32, it goes into the Scripts folder right in your Python installation,
for example, C:\Python25\Scripts . In either case, you need to make sure that
django-admin.py is in your PATH so it can be executed from the command line.
To create the project directory for your blog project, issue this django-admin.py
command:

cd into a directory where you’d like to store your code,
=======================================================
    django-admin.py startproject mysite
=======================================================    

startproject command akan membuat minimal 3 file berikut.
1. manage.py        : is a utility for working with this Django project.You can see from its
                        permissions flags in the directory listing that it is executable.
                        We run it in a moment.
2. setting.py       : is a file containing default settings for your project.These include
                        database information, debugging flags, and other important variables.
                        Any value in this file is available to any of your project’s 
                        installed apps—we show you the usefulness of that as we progress 
                        through this chapter.
3. urls.py          : is what’s known in Django as a URLconf, a configuration file that maps
                        URL patterns to actions your applications perform. URLconfs are an 
                        exciting and powerful feature of Django.
"""

