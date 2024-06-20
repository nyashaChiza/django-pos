import os
from pathlib import Path
from dotenv import load_dotenv
import pymysql
from decouple import config

pymysql.install_as_MySQLdb()
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config("DJANGO_SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://pos.tomorrow.co.ke",
    "https://pos.tomorrow.co.ke",
    "https://localhost",
]

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "crispy_forms",
    "crispy_bootstrap5",
    "django.contrib.staticfiles",
    "rest_framework",
]

LOCAL_APPS = [
    "customers",
    "pos",
    "products",
    "sales",
    "company",
    "inventory",
    "etims",
    "reports",
    "suppliers",
    "accounting",
    "expenses",
    "cloud",
    "purchases",
    "authentication",
    "onboarding",
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_pos.urls"
LOGIN_URL = "/users/login/"
# Route defined in authentication/urls.py
LOGIN_REDIRECT_URL = "authentication:home"
# Route defined in authentication/urls.py
LOGOUT_REDIRECT_URL = "authentication:login"

# ROOT dir for templates


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "company.context_processors.company_context"
            ],
        },
    },
]

WSGI_APPLICATION = "django_pos.wsgi.application"

# Database

MYSQL_DB_NAME = config("MYSQL_DB_NAME")
MYSQL_DB_USER = config("MYSQL_DB_USER")
MYSQL_DB_PASSWORD = config("MYSQL_DB_PASSWORD")
MYSQL_DB_HOST = config("MYSQL_DB_HOST")
MYSQL_DB_PORT = config("MYSQL_DB_PORT")
USE_MYSQL = config("USE_MYSQL", cast=bool)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql" if USE_MYSQL else "django.db.backends.sqlite3",
        "NAME": MYSQL_DB_NAME if USE_MYSQL else BASE_DIR / "db.sqlite3",
        "USER": MYSQL_DB_USER if USE_MYSQL else None,
        "PASSWORD": MYSQL_DB_PASSWORD if USE_MYSQL else None,
        "HOST": MYSQL_DB_HOST if USE_MYSQL else None,
        "PORT": MYSQL_DB_PORT if USE_MYSQL else None,
        # "OPTIONS": {"charset": "utf8mb4_general_ci", "use_unicode": True},
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Nairobi"

USE_I18N = True

USE_TZ = True


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Media Files
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# configuration for the license server
LICENSE_SERVER = "https://tomorrow.co.ke"
MY_COMPANY_NAME = "Tomorrow Solutions"
MY_COMPANY_ID = "1"