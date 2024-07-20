from dj_database_url import parse

from .base import *     # noqa: F401, F403
from .base import BASE_DIR, env, MIDDLEWARE

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

DATABASES = {
    "default": parse(env("DATABASE_URL")),
}

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

DEFAULT_FILE_STORAGE = 'myapp.storage_backends.FirebaseStorage'
MEDIA_URL = 'https://storage.googleapis.com/portfolio-374b7.appspot.com/'
MEDIA_ROOT = None

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
