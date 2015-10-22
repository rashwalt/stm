# Import sys (to adjust Python path)
import sys
# Import some utility functions
from os.path import abspath, basename, dirname, join, normpath
from django.contrib import messages

# #########################################################

# ##### PATH CONFIGURATION ################################

# Fetch Django's project directory
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Fetch the project_root
PROJECT_ROOT = dirname(DJANGO_ROOT)

# The name of the whole site
SITE_NAME = basename(DJANGO_ROOT)

# Collect static files here
STATIC_ROOT = join(PROJECT_ROOT, 'deploy', 'static')

# Collect media files here
MEDIA_ROOT = join(PROJECT_ROOT, 'deploy', 'media')

#  look for static assets here
STATICFILES_DIRS = [
    join(PROJECT_ROOT, 'static'),
]

# look for templates here
# This is an internal setting, used in the TEMPLATES directive
PROJECT_TEMPLATES = [
    join(PROJECT_ROOT, 'templates'),
    join(PROJECT_ROOT, 'templates', 'apps'),
]

# Add apps/ to the Python path
sys.path.append(normpath(join(PROJECT_ROOT, 'apps')))


# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = (
    # django admin bootstraped
    'django_admin_bootstrapped',

    'apps.ex_staticfiles',

    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django extension
    'django_extensions',

    # django-bootstrap3
    'bootstrap3',

    # django-pipeline
    'pipeline',

    # apps
    'apps.base.colorfield',
    'apps.base.navigation',
    'apps.memo',
)

# Middlewares
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

# Template stuff
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': PROJECT_TEMPLATES,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ##### SECURITY CONFIGURATION ############################

# secret key here
SECRET_KEY = 'j9+4_o9mvef8_kv&ono&0&f-v&)9qk_49@$o275198mo$q4him'

# These persons receive error notification
ADMINS = ()
MANAGERS = ADMINS


# ##### DJANGO RUNNING CONFIGURATION ######################

# The default WSGI application
WSGI_APPLICATION = '{}.wsgi.application'.format(SITE_NAME)

# The root URL configuration
ROOT_URLCONF = '{}.urls'.format(SITE_NAME)

# This site's ID
SITE_ID = 1

# The URL for static files
STATIC_URL = '/static/'

# The URL for media files
MEDIA_URL = '/media/'


# ##### DEBUG CONFIGURATION ###############################
DEBUG = False

ALLOWED_HOSTS = []


# ##### INTERNATIONALIZATION ##############################

LANGUAGE_CODE = 'ja'
TIME_ZONE = 'UTC'

# Internationalization
USE_I18N = True

# Localisation
USE_L10N = True

# enable timezone awareness by default
USE_TZ = True


# ##### DJANGO BOOTSTRAP 3 ################################

DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

BOOTSTRAP3 = {
    'jquery_url': 'https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js',
    'base_url': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/',
    'javascript_in_head': True,
    'theme_url': 'https://maxcdn.bootstrapcdn.com/bootswatch/3.3.5/flatly/bootstrap.min.css',
}

MESSAGE_TAGS = {
    messages.SUCCESS: 'alert-success success',
    messages.WARNING: 'alert-warning warning',
    messages.ERROR: 'alert-danger error'
}


# ##### DJANGO STATIC FILES ##############################

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

STATICFILES_IGNORES = (
    'debug_toolbar',
    'django_extensions',
    'bootstrap',
    'bootstrap-rtl',
)

# ##### DJANGO PIPELINE ##################################

PIPELINE_CSS = {
    'core': {
        'source_filenames': (
            'css/core.styl',
        ),
        'output_filename': 'css/core.min.css',
    },
    'starter': {
        'source_filenames': (
            'css/starter-template.styl',
        ),
        'output_filename': 'css/starter.min.css',
    },
}

PIPELINE_JS = {
    'core': {
        'source_filenames': (
            'js/core.js',
        ),
        'output_filename': 'js/core.min.js',
    }
}

PIPELINE_CSS_COMPRESSOR = None
PIPELINE_JS_COMPRESSOR = None

PIPELINE_COMPILERS = (
    'pipeline.compilers.coffee.CoffeeScriptCompiler',
    'pipeline.compilers.stylus.StylusCompiler',
)
PIPELINE_COFFEE_SCRIPT_BINARY = '/usr/local/bin/node /usr/local/bin/coffee'
PIPELINE_STYLUS_BINARY = '/usr/local/bin/node /usr/local/bin/stylus'
