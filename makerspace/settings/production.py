
try:
    from .common import *
except ImportError:
    pass

DEBUG = False

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


# Your local stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = ['makerspace.django.group','localhost', '127.0.0.1', ]
