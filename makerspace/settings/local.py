try:
    from .common import *
except ImportError:
    pass



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sw1b5!3e-ug1f#sdeacn7+c%(n6#2+5x2@q&iec%@-j%71$s)9'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['127.0.0.1', 'localhost',]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'doelf_makerspace',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'doelf',
        'PASSWORD': 'rAC9sFBS',
        'HOST': 'localhost',  # 'debian.fritz.box',
        # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',  # Set to empty string for default.
    }
}


