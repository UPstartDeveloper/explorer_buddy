"""
Django settings for explorer project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from dotenv import load_dotenv
import django_heroku
from django.urls import reverse

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(f'base dir: {BASE_DIR}')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
load_dotenv()
SECRET_KEY = str(os.getenv('SECURITY_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', False)

ALLOWED_HOSTS = [
    'explorer-buddy.herokuapp.com',
    'localhost',
]


# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notes.apps.NotesConfig',
    'accounts.apps.AccountsConfig',
    'crispy_forms'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'explorer.urls'

PROJECT_TEMPLATES_PATH = os.path.join(BASE_DIR, 'templates').replace('\\', '/')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # project templates
            PROJECT_TEMPLATES_PATH,
            os.path.join(PROJECT_TEMPLATES_PATH,
                         'partials').replace('\\', '/'),
            os.path.join(PROJECT_TEMPLATES_PATH,
                         'base_templates').replace('\\', '/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'explorer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

# redirect to create form when successfully authenticated users
LOGIN_REDIRECT_URL = 'notes:create_note_form'

# redirect back to login page on logout
LOGOUT_REDIRECT_URL = 'accounts:login'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.' +
            'UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# note settings
NOTE_TITLE_MAX_LENGTH = 600

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

LOCAL_CDN_PATH = os.path.join(os.path.dirname(BASE_DIR), 'static_cdn')

STATIC_ROOT = os.path.join(LOCAL_CDN_PATH, 'static')
STATIC_URL = '/static/'

# mock live cdn i.e. AWS S3
# LOCAL_CDN_PATH = os.path.join(os.path.dirname(BASE_DIR), 'static_cdn')
# STATIC_ROOT = os.path.join(LOCAL_CDN_PATH, 'static')

STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'static/'),  # represents the local version
 ]

# used to render images from ImageField in Note model
# credit goes to: Justin Mitchel at https://tinyurl.com/vofmamq
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(LOCAL_CDN_PATH, '/media/images')


# Settings for sending email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = str(os.getenv('EMAIL_USERNAME'))
EMAIL_HOST_PASSWORD = (
                       str(os.getenv('EMAIL_PASS_1')) + " " +
                       str(os.getenv('EMAIL_PASS_2')) + " " +
                       str(os.getenv('EMAIL_PASS_3')) + " " +
                       str(os.getenv('EMAIL_PASS_4'))
                      )

DEFAULT_FROM_EMAIL = os.getenv('EMAIL_USERNAME')

django_heroku.settings(locals())
