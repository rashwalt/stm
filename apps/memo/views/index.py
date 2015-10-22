from apps.base.views.generic import BaseTemplateView
from apps.base.navigation.enums import Navigation
from memo.models import Memo


class IndexView(BaseTemplateView):
    template_name = 'apps/memo/index.html'
    page_id = Navigation.home.page_id

    def get_context_data(self, **kwargs):
        return {
            'memo_list': Memo.objects.all(),
        }
