from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

WSGI_APPLICATION = 'config.wsgi.debug.application'

DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']