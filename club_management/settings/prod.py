from .common import *

DEBUG = False
ALLOWED_HOSTS = ['52.79.181.153']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'second',
        'USER': 'second',
        'PASSWORD': 'gjrjfl12!@',
    },
}