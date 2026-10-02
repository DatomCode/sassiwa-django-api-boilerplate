"""Production settings for the application."""

# pylint: disable=relative-beyond-top-level,wildcard-import
import os
from django.core.exceptions import ImproperlyConfigured

from .base import *


REQUIRED_ENVIRONMENT_VARIABLES = (
    "DJANGO_SECRET_KEY",
    "DB_NAME",
    "DB_HOST",
    "DB_PORT",
    "DB_USER",
    "DB_PASSWORD",
    "ALLOWED_HOSTS",
)

missing_variables = [
    variable
    for variable in REQUIRED_ENVIRONMENT_VARIABLES
    if not os.environ.get(variable)
]

if missing_variables:
    raise ImproperlyConfigured(
        "Missing required production environment variables: "
        + ", ".join(missing_variables)
    )


DEBUG = False
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"].split(",")
DATABASES["default"]["OPTIONS"]["sslmode"] = os.getenv("DB_SSLMODE", "require")
