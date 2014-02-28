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
SECRET_KEY = 'qgd-0(ckc^q+0w2(k%jxt8ywtapv-r-@6x-de2sb#$afzk*sqa'

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

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ('assets', os.path.join(BASE_DIR, 'static'))
)
