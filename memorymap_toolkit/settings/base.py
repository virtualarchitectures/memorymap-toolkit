"""
Django settings for memorymap_toolkit project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.forms',
    # Constance
    'constance.backends.database',
    # Memory Map Toolkit
    'mmt_map',
    'mmt_pages',
    'mmt_api',
    # 3rd Party
    'easy_thumbnails',
    'filer',
    'mptt',
    'ckeditor',
    'ckeditor_uploader',
    'constance',
    'debug_toolbar',
    'taggit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'memorymap_toolkit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'memorymap_toolkit.context_processors.site_settings'
            ],
        },
    },
]

WSGI_APPLICATION = 'memorymap_toolkit.wsgi.application'





# Caching. The dynamically-created map tiles are cached using memcached so the load on the database isn't too heavy for larger maps

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR.child('static')

STATICFILES_DIRS = [
    BASE_DIR.child('project_static'),
]

# Media Settings

MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'


# Forms (for custom map widget)

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'


### App-Specific Settings ###

# Django-ckeditor Settings

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Format', 'Bold', 'Italic', 'Underline'],
            ['BulletedList', 'Blockquote'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'SpecialChar'],
            ['RemoveFormat', 'Source']
        ]
    },
}

# Easy Thumbnails

THUMBNAIL_ALIASES = {
    '': {
        'site_small': {'size': (300, 175), 'crop': 'smart', 'upscale': True},
        'banner': {'size': (600, 350), 'crop': 'smart', 'upscale': True},
    },
}

# Constance

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_ADDITIONAL_FIELDS = {
    'image_field': ['django.forms.ImageField', {}],
    'file_field': ['django.forms.FileField', {}]
}

CONSTANCE_CONFIG = {
    'SITE_TITLE': ('Memory Map Toolkit', 'The name of your site'),
    'LOGO_IMAGE': ('default.png', 'You can upload an image to display in the menu bar here', 'image_field'),
    'MAP_CENTER_LATITUDE': (0.0, 'The latitude of the centre point of the map'),
    'MAP_CENTER_LONGITUDE': (0.0, 'The longitude of the centre point of the map'),
    'ZOOM': (15.5, 'The default zoom level of the map'),
    'MIN_ZOOM': (9.5, 'The lowest zoom level of the map'),
    'MAX_ZOOM': (18.4, 'The highest zoom level of the map'),
    'BASE_MAP_STYLE_URL': ('/static/js/default_map_style.json', 'URL to a MapboxGL Map style. If using maps hosted with MapBox, use the style API as documented here: https://docs.mapbox.com/api/maps/#retrieve-a-style'),
    'BASE_MAP_STYLE_FILE': ('default.json', 'As an alternative to a MapboxGL style link, you can also upload a MapBoxGL StyleJson file to customise the look of your base map. Uploading a file will override the BASE_MAP_STYLE settings', 'file_field'),
    'MAPTILER_KEY': ('', 'The default map style uses Ordnance Survey Open Zoomstack tiles hosted with Maptiler Cloud. To use these, you need to sign up for a free account and copy your user key here.'),
    'MAPBOX_KEY': ('', 'If you have uploaded a map style file created in MapBox, put your key here'),
    'SCALE': ('metric', 'The units to use for the map scale widget'),
    'PITCH': (0, 'The pitch of the map viewport'),
    'BEARING': (0, 'The bearing of the map viewport'),
    'WELCOME_MESSAGE': ('Welcome to the Memory Map Toolkit', 'The message that displays when the site loads'),
    'SITE_METADATA': ('', 'Metadata in json-ld format. Adding this will improve the visibility of your site in search results'),
    'SWITCHABLE_LAYERS': ('', 'A comma-separated list of map layer IDs from your map style. This will allow visitors to your site to switch layers on and off from the menu bar. Particularly useful if you are using raster layers, for example for showing historic maps.'),
    'CUSTOM_CSS': ('default.css', 'Upload a css file to customise the look of your Memory Map', 'file_field'),
}


# Django Debug Toolbar

INTERNAL_IPS = [
    '127.0.0.1',
    '10.0.2.15',
    '10.0.2.2',
]