"""
Django settings for mkdir project.
"""

import os
from pathlib import Path
import dj_database_url
import cloudinary
import sys

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure--%e9w2x+me4-vp83xb1=q+w4s7!v339rnzf8t-hfy6y8vxkbc(')

# Environment detection
ON_RENDER = os.environ.get('RENDER', False)
DEVELOPMENT_MODE = not ON_RENDER

if DEVELOPMENT_MODE:
    DEBUG = True
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']
else:
    DEBUG = False
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '.onrender.com').split(',')

# Application definition
INSTALLED_APPS = [
    'cloudinary',
    'cloudinary_storage',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]

# Cloudinary configuration
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dydfafccz',
    'API_KEY': '739943485751172',
    'API_SECRET': 'g_9doBvNhKbW-XyO34QOqmTTvTk'
}

cloudinary.config(
    cloud_name="dydfafccz",
    api_key="739943485751172",
    api_secret="g_9doBvNhKbW-XyO34QOqmTTvTk",
    secure=True
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mkdir.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mkdir.wsgi.application'

# Database configuration
if DEVELOPMENT_MODE:
    # Local development: SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # Production: PostgreSQL with better error handling
    DATABASE_URL = os.environ.get('DATABASE_URL')
    if not DATABASE_URL:
        # Fallback to hardcoded URL if environment variable is not set
        DATABASE_URL = "postgresql://wallpaper_g7kj_user:iA59in3Wvuj4nZreiWbAYVU5LtLTDlNW@singapore-postgres.render.com:5432/wallpaper_g7kj"
        print("WARNING: Using hardcoded DATABASE_URL. Set environment variable for security.")
    
    DATABASES = {
        "default": dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            ssl_require=True,
        )
    }

# Password validation
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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Storage configuration
if DEVELOPMENT_MODE:
    # Local development: Use local storage
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
else:
    # Production: Use Cloudinary
    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticCloudinaryStorage'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'