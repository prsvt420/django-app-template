import os
from pathlib import Path
from typing import Dict, List, Optional

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY: Optional[str] = os.getenv("SECRET_KEY")

DEBUG: bool = os.getenv("DEBUG") == "True"

ALLOWED_HOSTS: List[str] = [
    "127.0.0.1",
    "...",
]

INTERNAL_IPS: List[str] = [
    "127.0.0.1",
]

INSTALLED_APPS: List[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "csp",
    "core",
]

MIDDLEWARE: List[str] = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "csp.middleware.CSPMiddleware",
]

ROOT_URLCONF: str = "django_app_template.urls"

TEMPLATES: List[Dict] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION: str = "django_app_template.wsgi.application"

DATABASES: Dict = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": "localhost" if DEBUG else os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT", default=5432),
    }
}

AUTH_PASSWORD_VALIDATORS: List[Dict] = [
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

LANGUAGE_CODE: str = "ru-RU"

TIME_ZONE: str = "UTC"
USE_I18N: bool = True
USE_TZ: bool = True

STATIC_URL: str = "static/"
STATICFILES_DIRS: List = [
    BASE_DIR / "static",
]
STATIC_ROOT: Path = BASE_DIR / "staticfiles"

MEDIA_URL: str = "media/"
MEDIA_ROOT: Path = BASE_DIR / "media"

FIXTURE_DIRS: List = [
    "fixtures",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_HOST: str = "smtp.gmail.com"
EMAIL_PORT: int = 587
EMAIL_USE_TLS: bool = True
EMAIL_HOST_USER: Optional[str] = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD: Optional[str] = os.getenv("EMAIL_HOST_PASSWORD")

SITE_NAME: str = "Django App Template"

CELERY_BROKER_URL: Optional[str] = (
    "redis://127.0.0.1:6379" if DEBUG else os.getenv("REDIS_LOCATION")
)
CELERY_RESULT_BACKEND: Optional[str] = (
    "redis://127.0.0.1:6379" if DEBUG else os.getenv("REDIS_LOCATION")
)
CELERY_TIMEZONE: str = "Europe/Moscow"

CSP_DEFAULT_SRC: List = ["'self'"]
CSP_IMG_SRC: List = ["'self'", "data:", "https://cdn.redoc.ly"]
CSP_SCRIPT_SRC: List = ["'self'", "'unsafe-inline'"]
CSP_STYLE_SRC: List = ["'self'", "https://fonts.googleapis.com/", "'unsafe-inline'"]
CSP_FONT_SRC: List = ["'self'", "https://fonts.gstatic.com"]
CSP_WORKER_SRC: List = ["'self'", "blob:"]
