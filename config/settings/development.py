"""Development settings for the application."""

import os

# pylint: disable=relative-beyond-top-level,wildcard-import
from .base import *

DEBUG = True
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-development-only")

ALLOWED_HOSTS = ["*"]
DATABASES["default"]["OPTIONS"]["sslmode"] = os.getenv("DB_SSLMODE", "disable")
