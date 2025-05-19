import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')  # Will be overridden by env var

DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']  # Allow all hosts for Railway deployment

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'ckeditor',
    'core',
    'whitenoise.runserver_nostatic',  # Add whitenoise for static files
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add whitenoise middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CSRF settings for Railway - allow frontend to make POST requests
CSRF_TRUSTED_ORIGINS = []
RAILWAY_DOMAIN = os.getenv('RAILWAY_DOMAIN', '')
if RAILWAY_DOMAIN:
    CSRF_TRUSTED_ORIGINS.append(f'https://{RAILWAY_DOMAIN}')

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'portfolio.wsgi.application'

# Database configuration for Railway (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('PGDATABASE', 'postgres'),
        'USER': os.getenv('PGUSER', 'postgres'),
        'PASSWORD': os.getenv('PGPASSWORD', ''),
        'HOST': os.getenv('PGHOST', 'localhost'),
        'PORT': os.getenv('PGPORT', '5432'),
    }
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
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Media file serving (temporary solution for Railway)
# In production, it's better to use S3 or similar service
if not DEBUG:
    # This will allow URLs like /media/example.jpg to be served by Django directly
    # Not ideal for production but will work for a portfolio site with limited uploads
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# CORS settings - Allow your Vercel frontend to access your API
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    'http://localhost:5000',
    'http://127.0.0.1:5000',
]

# Add your Vercel domain here
VERCEL_DOMAIN = os.getenv('VERCEL_DOMAIN', '')
if VERCEL_DOMAIN:
    CORS_ALLOWED_ORIGINS.append(f'https://{VERCEL_DOMAIN}')
    CORS_ALLOWED_ORIGINS.append(f'http://{VERCEL_DOMAIN}')

# Allow all origins if needed (less secure but simplifies development)
# CORS_ALLOW_ALL_ORIGINS = True  # Uncomment if you're having CORS issues

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security settings for production
if not DEBUG:
    # HTTPS settings
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True