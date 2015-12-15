import os
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '+n_bzj+(x_c)n3su@2a3q%_wad0y!mcu3b+ec-2d^nof-l)50_'
DEBUG = True
INSTALLED_APPS = []
ROOT_URLCONF = 'language_test.urls'
WSGI_APPLICATION = 'language_test.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# The settings that matter to the bug
USE_I18N = True
LANGUAGE_CODE = 'xxx'
LANGUAGES = [
    ('xxx', _('Xxx')),
]
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]
