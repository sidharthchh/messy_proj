from .common import *

DEBUG = False
ALLOWED_HOSTS = []
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = False

# Configure logentries only if LOGENTRIES_KEY is defined in settings
if os.environ.get("LOGENTRIES_KEY", ''):
    LOGGING['handlers']['logentries'] = {
        'level': 'INFO',
        'token': os.environ.get("LOGENTRIES_KEY", ''),
        'class': 'logentries.LogentriesHandler',
        'formatter': 'verbose'
    }

    LOGGING['loggers']['messy-proj']['handlers'] = ['console', 'file', 'logentries']
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')

ALLOWED_HOSTS = ALLOWED_HOSTS.append(os.environ.get('ALLOWED_HOST'))
