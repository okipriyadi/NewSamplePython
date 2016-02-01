"""
let's open the settings.py file
in the project folder and see what it contains:



# Build paths inside the project like this: os.path.join(BASE_DIR,...)

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')9c8g--=vo2*rh$9f%=)=e+@%7e%xe8jptgpfe+(90t7uurfy0'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG             = True
TEMPLATE_DEBUG     = True
ALLOWED_HOSTS = []
# Application definition
INSTALLED_APPS = (
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                )

MIDDLEWARE_CLASSES = (
                    'django.contrib.sessions.middleware.SessionMiddleware',
                    'django.middleware.common.CommonMiddleware',
                    'django.middleware.csrf.CsrfViewMiddleware',
                    'django.contrib.auth.middleware.AuthenticationMiddleware',
                    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
                    'django.contrib.messages.middleware.MessageMiddleware',
                    'django.middleware.clickjacking.XFrameOptionsMiddleware',
                    )
ROOT_URLCONF = 'django_bookmarks.urls'
WSGI_APPLICATION = 'django_bookmarks.wsgi.application'
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
            'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
            }
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'




What concerns us now is configuring the database. we have to specify what database
system we are going to use. This is controlled by the DATABASE_ENGINE variable. If
you have SQLite installed, set the variable to 'sqlite3' . Otherwise, pick the value
that matches your database engine from the comment next to the variable name.
Next is the database name. Keep the database name default, as it is. On the other
hand, if you are using a database server, you need to do the following:
    • Enter the relevant information for the database: username, password, host,
      and port. (SQLite does not require any of these.)
    • Create the actual database inside the database server, as Django won't do this
      by itself. In MySQL, for example, this is done through the mysql command
      line utility or phpMyAdmin.

Finally, we will tell Django to populate the configured database with tables. Although
we haven't created any tables for our data yet (and won't do so until the next chapter),
Django requires several tables in the database for some of its features to function
properly. Creating these tables is as easy as issuing the following command:
===========================================================
   $ python manage.py syncdb
===========================================================

If everything is correct, status messages will scroll on the screen, indicating that
tables are being created. When prompted for the superuser account, enter your
preferred username, email, and password. If, on the other hand, the database is
misconfigured, an error message will be printed to help you troubleshoot the issue.
With this done, we are ready to launch our application.

untuk menjalankannya gunakan perintah
=============================================================================================
python manage.py runserver
=============================================================================================


"""