import os
DIRNAME = os.path.dirname(__file__)

DEFAULT_CHARSET = 'utf-8'

test_engine = os.environ.get("TAGGING_TEST_ENGINE", "django.db.backends.sqlite3")

DATABASES = {
    'default': {
        'ENGINE': test_engine,
        'NAME': os.environ.get("TAGGING_DATABASE_NAME", "tagging_test"),
        'USER': os.environ.get("TAGGING_DATABASE_USER", ""),
        'PASSWORD': os.environ.get("TAGGING_DATABASE_PASSWORD", ""), 
        'HOST': os.environ.get("TAGGING_DATABASE_HOST", "localhost"),
    }
}

if test_engine == "django.db.backends.sqlite3":
    DATABASES['default']['NAME'] = os.path.join(DIRNAME, 'tagging_test.db')
    DATABASES['default']['HOST'] = ""
elif test_engine == "django.db.backends.mysql":
    DATABASES['default']['PORT'] = os.environ.get("TAGGING_DATABASE_PORT", 3306)
elif test_engine == "django.db.backends.postgresql_psycopg2":
    DATABASES['default']['PORT'] = os.environ.get("TAGGING_DATABASE_PORT", 5432)


INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'tagging',
    'tagging.tests',
)
