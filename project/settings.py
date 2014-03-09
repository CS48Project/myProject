"""
Django settings for project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
from django.utils.crypto import get_random_string
SECRET_KEY = os.environ.get("SECRET_KEY", get_random_string(50, "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'food/templates'),
                 os.path.join(BASE_DIR, 'authentication/templates')]

AUTH_PROFILE_MODULE = 'django.contrib.auth.models.User'
MAILER_EMAIL_BACKEND = 'django_ses.SESBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ivwhattoeat@gmail.com'
EMAIL_HOST_PASSWORD = 'costanbro'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# URL for @login_required decorator to use
LOGIN_URL = '/accounts/login/'

SITE_ID = 1

SESSION_COOKIE_AGE = 1209600

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'food',
    'authentication',
    'ratings',
    'django_comments',
    'pytz',
    'gunicorn',
    'storages',
    'require_s3',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'static')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = 'staticfiles'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
        }
    }
}

from os import environ
from urlparse import urlparse

if environ.has_key('DATABASE_URL'):
    url = urlparse(environ['DATABASE_URL'])
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    }

# Use Amazon S3 for storage for uploaded media files.
DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"

# Use Amazon S3 for static files storage.
STATICFILES_STORAGE = "require_s3.storage.OptimizedCachedStaticFilesStorage"

# Amazon S3 settings.
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")
AWS_AUTO_CREATE_BUCKET = True
AWS_HEADERS = {
    "Cache-Control": "public, max-age=86400",
}
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_SECURE_URLS = True
AWS_REDUCED_REDUNDANCY = False
AWS_IS_GZIPPED = False
AWS_PRELOAD_METADATA = True

# Cache settings.
CACHES = {
    # Long cache timeout for staticfiles, since this is used heavily by the optimizing storage.
    "staticfiles": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "TIMEOUT": 60 * 60 * 24 * 365,
        "LOCATION": "staticfiles",
    },
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}
