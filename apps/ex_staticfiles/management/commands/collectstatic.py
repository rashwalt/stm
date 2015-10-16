from django.conf import settings
from django.contrib.staticfiles.management.commands.collectstatic import \
    Command as CollectStaticCommand


print('test')

class Command(CollectStaticCommand):
    def set_options(self, **options):
        super(Command, self).set_options(**options)
        if hasattr(settings, 'STATICFILES_IGNORES'):
            ignore_patterns = self.ignore_patterns
            ignore_patterns.extend(settings.STATICFILES_IGNORES)
            self.ignore_patterns = list(set(ignore_patterns))
