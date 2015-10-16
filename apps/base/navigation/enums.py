from enum import Enum
from django.core.urlresolvers import reverse


class Navigation(Enum):
    home = (1, 'Home', 'memo_index')
    about = (2, 'About', 'memo_index')
    contact = (3, 'Contact', 'memo_index')

    @property
    def page_id(self):
        return self.value[0]

    @property
    def page_name(self):
        return self.value[1]

    @property
    def url(self):
        return reverse(self.value[2])
