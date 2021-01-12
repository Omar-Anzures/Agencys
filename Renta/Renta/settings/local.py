from .base import*

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_USER'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

#EMAIL SETTINGS

EMAIL_USE_TLS = True
#si queremos de otro tipo de correo debemos de verificar cual es la extension
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = get_secret('EMAIL')
EMAIL_HOST_PASSWORD = get_secret('PASS_EMAIL')
EMAIL_PORT = 587