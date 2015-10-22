from enum import Enum
from django.core.urlresolvers import reverse


class Navigation(Enum):
    home = (1, 'ホーム', 'memo_index')
    label = (2, 'タグ管理', 'memo_label_list')

    @property
    def page_id(self):
        return self.value[0]

    @property
    def page_name(self):
        return self.value[1]

    @property
    def url(self):
        return reverse(self.value[2])
