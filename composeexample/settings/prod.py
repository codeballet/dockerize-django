import os
from .base import *

# Set environment variable:
# export DJANGO_SETTINGS_MODULE="composeexample.settings.prod"

# Deployment settings:
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5-pwk@)k^nupu-0uw04_xx$*z^#0)%tbapx$3t!gab$!0*_(ta'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Add webdomain or server IP
ALLOWED_HOSTS = ["localhost"]

# collect static files with command: 'python manage.py collectstatic'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
