from .base import *     # noqa: F401, F403
from .base import env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

env.list('ALLOWED_HOSTS')

DATABASES = {
    "default": env("DATABASE_URL"),
}
