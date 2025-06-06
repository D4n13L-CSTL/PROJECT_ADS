"""
Django settings for ProyectoPublicidad project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import urlparse
# Build paths inside the project like this: BASE_DIR / 'subdir'.
import os
load_dotenv()
from decouple import config
import cloudinary
import cloudinary.uploader
import cloudinary.api


CLERK_API_KEY = config("CLERK_SECRET_KEY")

CLERK_DOMAIN = config("CLERK_DOMAIN")
CLOUD_NAME = config("CLOUD_NAME")
API_KEY = config("API_KEY")
API_SECRET = config("API_SECRET")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



CLOUDINARY_STORAGE = {
    'CLOUD_NAME': CLOUD_NAME,
    'API_KEY': API_KEY,
    'API_SECRET': API_SECRET,
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zbqf3jz!)fw(6@oqgxcjga5*o*lhx0gtg-4e(0d=&j-=zta0an'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'corsheaders',
    'django_extensions',    
    'rest_framework',
    'drf_spectacular',
    'app_init',
    'app_dashboard',
    'app_campañas',
    'app_perfiles',
    'app_publicidades',
    'app_pautasMaker',
    'app_wallet',
    'rest_framework_simplejwt'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Debe ir primero
    'django.middleware.common.CommonMiddleware'
]

ROOT_URLCONF = 'ProyectoPublicidad.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'ProyectoPublicidad.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


tmpPostgres = urlparse(os.getenv("DATABASE_URL"))




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': tmpPostgres.path.replace('/', ''),
        'USER': tmpPostgres.username,
        'PASSWORD': tmpPostgres.password,
        'HOST': tmpPostgres.hostname,
        'PORT': 5432,
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
"""STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  # Asegura que Django reconozca la carpeta static/
]"""

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',


        'DEFAULT_AUTHENTICATION_CLASSES': [
        'middleware.jwt_cookie_auth.ClerkAuthentication',
    ],
        
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',

    ),
    'EXCEPTION_HANDLER': 'middleware.handler.custom_exception_handler',


}


CORS_ALLOW_ALL_ORIGINS = True

LOGIN_URL = '/'  # O cualquier URL de login que tengas configurada


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
