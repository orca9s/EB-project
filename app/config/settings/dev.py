from .base import *
secrets = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))
DEBUG = True

# django-storages
INSTALLED_APPS += [
    'storages',
]

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'config.wsgi.dev.application'

# DB
DATABASES = secrets['DATABASES']

STATICFILES_STORAGE = 'config.storages.S3StaticStorage'

# Media
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']
DEFAULT_FILE_STORAGE = 'config.storages.S3DefaultStorage'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')