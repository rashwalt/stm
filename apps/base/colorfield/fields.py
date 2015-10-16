#!/usr/bin/env python

import re

from django import forms
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

color_re = re.compile('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
validate_color = RegexValidator(color_re, _('Enter a valid color.'), 'invalid')


class ColorWidget(forms.TextInput):
    class Media:
        js = ('https://cdnjs.cloudflare.com/ajax/libs/bootstrap-colorpicker/2.3.0/js/bootstrap-colorpicker.min.js',)
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/bootstrap-colorpicker/2.3.0/css/bootstrap-colorpicker.min.css',)
        }
        
    def render(self, name, value, attrs=None):
        script = """
<script>
    $(function(){
        $('.%s').colorpicker();
    });
</script>
""" % ('id_group_{}'.format(name))

        super_render = super(ColorWidget, self).render(name, value, attrs)

        return_html = """
<div class="input-group %s">
%s
<span class="input-group-addon"><i></i></span>
</div>
%s
""" % ('id_group_{}'.format(name), super_render, script)
        return mark_safe(return_html)


class ColorField(models.CharField):
    default_validators = [validate_color]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorWidget
        return super(ColorField, self).formfield(**kwargs)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^apps\.base\.colorfield\.fields\.ColorField"])
except ImportError:
    pass

# vim: et sw=4 sts=4
