# -*- coding: utf-8 -*-
import os

PROJECT_ROOT = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	# ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': 'test-project.db',
			}
		}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Warsaw'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 2

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'hdaw2jet30@z0sm+zl$y_+8vrem2-mih5)(e^d@ng8@6m6wfth'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
#	 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
#	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'mamona',
	'mamona.backends.dummy',
	'mamona.backends.paypal',
	'order',
	'sales',
)

MAMONA_ACTIVE_BACKENDS = (
	'dummy',
	'paypal',
)
MAMONA_BACKENDS_SETTINGS = {
	'paypal': {
		'url': 'https://www.paypal.com/cgi-bin/webscr',			# real payments URL
#		'url': 'https://www.sandbox.paypal.com/cgi-bin/webscr',	# test payments URL
#		'return_url': 'http://www.example.com/success/',		# global override
		'email': 'michal.salaban@gmail.com',
	},
}

try:
	execfile(os.path.join(PROJECT_ROOT, 'local_settings.py'))
except IOError:
	pass
