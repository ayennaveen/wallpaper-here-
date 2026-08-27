import os
from pathlib import Path
import dj_database_url
import cloudinary

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent
REACT_BUILD_DIR = BASE_DIR / 'frontend' / 'dist'

# Security
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure--%e9w2x+me4-vp83xb1=q+w4s7!v339rnzf8t-hfy6y8vxkbc(')
DEBUG = True
ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']

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
    'corsheaders', # Added for React
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
    'corsheaders.middleware.CorsMiddleware', # Moved high up
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
        # Combined both React build dir and your old template dir
        'DIRS': [REACT_BUILD_DIR, os.path.join(BASE_DIR, 'template')],
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

WSGI_APPLICATION = 'mkdir.wsgi.application'

# Database configuration
if os.environ.get('RENDER', False):
    DATABASE_URL = os.environ.get('DATABASE_URL')
    if DATABASE_URL:
        DATABASES = {
            'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600, ssl_require=True)
        }
    else:
        DATABASES = {
            'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3'}
        }
else:
    DATABASES = {
        'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3'}
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files configuration (Combined)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    REACT_BUILD_DIR, # Django will check here for React assets
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage' if DEBUG else 'cloudinary_storage.storage.StaticCloudinaryStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:3000", 
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000",
]