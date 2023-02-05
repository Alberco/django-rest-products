from .base import *

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangorestfull',
        'USER': 'postgres',
        'PASSWORD': 'callofduty',
        'HOST': '127.0.0.1',
        'PORT': '5433   ',
    }
}


STATIC_URL = 'static/'