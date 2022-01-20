"""
Django settings for stranalyze project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import environ

from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env(DEBUG=(bool,False))
env.read_env(os.path.join(BASE_DIR,'.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['stranalyze.com','www.stranalyze.com','localhost',env('IP_ADDLESS')]

# Application definition

INSTALLED_APPS = [
    'accounts',
    'timeline.apps.TimelineConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.forms',
    'django.contrib.sites',
    'widget_tweaks',
    'allauth',
    'allauth.account',
    'bootstrap4',
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


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR, 'templates', 'allauth')
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':env('DB_NAME_SQL'),
        'USER':env('DB_USER_SQL'),
        'PASSWORD':env('DB_PASSWORD_SQL'),
        'HOST':env('DB_HOST_SQL'),
        'PORT':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ACCOUNT_FORMS = {
    'login' : 'accounts.forms.MyLoginForm',
    'signup' : 'accounts.forms.SignupForm',
    'password_reset_from_key' : 'accounts.forms.MyPasswordResetFromKeyForm',
    'password_reset' : 'accounts.forms.MyPasswordResetForm',
}


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'app/static'),
)

#STATICFILES_DIRS = [
#    BASE_DIR /'static'
#]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

MESSAGE_TAGS = {
    messages.ERROR: 'alert alert-danger',
    messages.WARNING: 'alert alert-warning',
    messages.SUCCESS: 'alert alert-success',
    messages.INFO: 'alert alert-info',
}

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

AUTH_USER_MODEL = 'accounts.CustomUser'

SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
LOGIN_URL = '/login/'
ACCOUNT_SIGNUP_REDIRECT_URL = 'account_login'
LOGIN_REDIRECT_URL = 'timeline:index'
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
DEFAULT_FROM_EMAIL = env('EMAIL_HOST_USER')
DEFAULT_AUTO_FIELD='django.db.models.AutoField'
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT= 180
FRONTEND_URL = "https://stranalyze.com"

SILENCED_SYSTEM_CHECKS = ["auth.W004"]
FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')
#SECURE_SSL_REDIRECT = True

