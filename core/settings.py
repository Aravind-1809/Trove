import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = eval(os.environ.get('DEBUG'))
SECRET_KEY = os.environ.get('SECRET_KEY')

PROJECT_NAME = os.environ.get('PROJECT_NAME')
ENVIRONMENT = os.environ.get('ENVIRONMENT')
ALLOWED_HOSTS = eval(os.environ.get('ALLOWED_HOSTS'))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY = [
    'cookielaw'
]

APPS = [
    'web'
]

INSTALLED_APPS += THIRD_PARTY + APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('templates'), BASE_DIR.joinpath('templates/web')],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# SSL SETTINGS
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', os.environ.get('SECURE_PROXY_SSL_HEADER'))
# SECURE_SSL_REDIRECT = eval(os.environ.get('SECURE_SSL_REDIRECT'))
# SESSION_COOKIE_SECURE = eval(os.environ.get('SESSION_COOKIE_SECURE'))
# CSRF_COOKIE_SECURE = eval(os.environ.get('CSRF_COOKIE_SECURE'))

# SMTP authentication information for EMAIL_HOST.
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_SUBJECT_PREFIX = 'Trove Research - '

# Default mail from
SENDER = f'Trove Research<{os.environ.get("EMAIL_HOST_USER")}>'
RECEIVERS = eval(os.environ.get('EMAIL_DEFAULT_RECEIVERS'))


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR.joinpath('static')
]
STATIC_ROOT = BASE_DIR.joinpath('staticfiles')

# Media files
MEDIA_ROOT = BASE_DIR.joinpath('media')

MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'info': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR.joinpath('logs/info.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'verbose'
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR.joinpath('logs/error.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'info': {
            'handlers': ['info'],
            'level': 'DEBUG',
            'propagate': True
        },
        'error': {
            'handlers': ['error', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True
        }
    }
}
