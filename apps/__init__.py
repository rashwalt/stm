# default global setting
import os

from django.template.base import add_to_builtins

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stm.settings")

# add_to_builtins('bootstrap3.templatetags.bootstrap3')
