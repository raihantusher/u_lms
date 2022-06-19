from .base import *


DEBUG = False

ALLOWED_HOSTS = ["tobuy.click", "www.tobuy.click"]
AUTH_USER_MODEL = 'accounts.Account'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATICFILES_DIRS = [ 'static/']
STATIC_URL = 'static/'
STATIC_ROOT = "/var/www/tobuy/static/"
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field


# Base url to serve media files
MEDIA_URL = '/media/'

# Path where media is stored
MEDIA_ROOT = "/var/www/tobuy/media/"



from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mail_blaster',
        'USER': 'mail_blaster',
        'PASSWORD': '24f6e3dc1bbc5a5dfb1e5c6481b94eb7',
        'HOST': 'cloud.foxstall.com',
        'PORT': '5432',
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "mail.devlink.click"
EMAIL_PORT = 587
EMAIL_HOST_USER  = "trisha@devlink.click"
DEFAULT_FROM_EMAIL= "DevLink <no-reply@devlink.click>"
EMAIL_HOST_PASSWORD = "admin1234@$$"

EMAIL_USE_TLS = True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.tobuy.click"
EMAIL_PORT =  '25'
EMAIL_HOST_USER  = ""
DEFAULT_FROM_EMAIL= "DevLink <root@tobuy.click>"
EMAIL_HOST_PASSWORD = ""

EMAIL_USE_TLS = True