import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'ei18lz6)9v5_yvm0g%gdol3^vc%j%y@fr%@%a^ds45(#2r63wi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS   = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'geo_location',
    'leaflet',
    'djgeojson',
]
MIDDLEWARE       = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF     = 'geo_django.urls'
TEMPLATES        = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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
WSGI_APPLICATION = 'geo_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE'    : 'django.contrib.gis.db.backends.postgis',
        'NAME'      : 'locations',
        'USER'      : 'anup',
        'PASSWORD'  : 'Anup@123',
        'HOST'      : 'localhost',
        'PORT'      : '5432'
    }
}

# Leaflet Js Config
LEAFLET_CONFIG = {
    'DEFAULT_CENTER'    : (40.422773,-103.914703), # SET DEFAULT PIN LOCATION
    'DEFAULT_ZOOM'      : 4,
    'MAX_ZOOM'          : 15,
    'MIN_ZOOM'          : 3,
    'SCALE'             :'both',
    'ATTRIBUTION_PREFIX':'Anup'
}

# Django GIS Serializer
SERIALIZATION_MODULES = {
    "geojson": "django.contrib.gis.serializers.geojson",
 }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE   = 'en-us'
TIME_ZONE       = 'UTC'
USE_I18N        = True
USE_L10N        = True
USE_TZ          = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

