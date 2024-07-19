from dj_database_url import parse

from .base import *     # noqa: F401, F403
from .base import env, MIDDLEWARE

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

DATABASES = {
    "default": parse(env("DATABASE_URL")),
}

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
