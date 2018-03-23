import os

# You must add this file to gitignore

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOCAL_DATABASE_SETTING = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}
