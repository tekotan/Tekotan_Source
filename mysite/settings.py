"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY
SECURE_BROWSER_XSS_FILTER = False  # True
SESSION_COOKIE_SECURE = True  # True
SECURE_SSL_REDIRECT = False  # True
CSRF_COOKIE_SECURE = True  # False
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
# KEY_FILE = Path("./tekotan.pythonanywhere.com/mysite/key.txt").absolute()
# EMAIL_FILE = Path("./tekotan.pythonanywhere.com/mysite/email.txt").absolute()
if os.path.isdir("tekotan.pythonanywhere.com/"):
    KEY_FILE = Path("./tekotan.pythonanywhere.com/mysite/key.txt").absolute()
    EMAIL_FILE = Path("./tekotan.pythonanywhere.com/mysite/email.txt").absolute()

else:
    KEY_FILE = Path("./mysite/key.txt").absolute()
    EMAIL_FILE = Path("./mysite/email.txt").absolute()



SECRET_KEY = KEY_FILE.read_text().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["www.tekotan.com", "127.0.0.1"]
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "b.tanish@tugun.net"
EMAIL_HOST_PASSWORD = EMAIL_FILE.read_text().strip()
DEFAULT_FROM_EMAIL = "noreply@tekotan.com"
EMAIL_PORT = 587

# Application definition

INSTALLED_APPS = [
    # "SentimentAnalysis.apps.SentimentanalysisConfig",
    "calculator.apps.CalculatorConfig",
    #    'recipe_extraction.apps.RecipeExtractionConfig',
    "work_experience.apps.WorkExperienceConfig",
    "other_projects.apps.OtherProjectsConfig",
    "tensorflow_projects.apps.TensorflowProjectsConfig",
    "poe_projects.apps.POEProjectsConfig",
    "csa_projects.apps.CSAProjectsConfig",
    "csp_projects.apps.CSPProjectsConfig",
    "signup.apps.SignupConfig",
    "tekotan.apps.TekotanConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "about_me.apps.AboutMeConfig",
    "career_exploration.apps.CareerExplorationConfig",
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.static",
            ]
        },
    }
]

WSGI_APPLICATION = "mysite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = "static/"
import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, "..\static")

# CORS
CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    'http://netlogoweb.org',
)

