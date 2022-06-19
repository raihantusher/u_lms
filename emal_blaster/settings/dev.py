from .base import *


DEBUG = True

AUTH_USER_MODEL = 'accounts.Account'


# media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'email_blaster',
        'USER': 'postgres',
        'PASSWORD': 'admin1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = 'a9c6c4bbf3d1c0'
EMAIL_HOST_PASSWORD = '65945b4b7e0c34'
EMAIL_PORT = '2525'
EMAIL_USE_TLS = True