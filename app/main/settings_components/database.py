import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database',
        'USER': 'root',
        'HOST': 'mysql',
        'PASSWORD': 'secret',
        'PORT': 3306,
    }
}
