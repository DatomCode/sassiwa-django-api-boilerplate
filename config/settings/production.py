"""Production settings for the application."""

# pylint: disable=relative-beyond-top-level,wildcard-import
from .base import *
import os


DEBUG = False


ALLOWED_HOSTS = os.environ.get(
    "ALLOWED_HOSTS",
    ""
).split(",")