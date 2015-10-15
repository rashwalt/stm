# Import some utility functions
from os.path import join
# Fetch our common settings
from .base import *

# #########################################################

# ##### DEBUG CONFIGURATION ###############################
DEBUG = True


# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(PROJECT_ROOT, 'tmp', 'develop.sqlite3'),
    }
}

# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS += (

)
