from apps.base.views.generic import BaseTemplateView
from apps.base.navigation.enums import Navigation


class IndexView(BaseTemplateView):
    template_name = 'apps/memo/index.html'
    page_id = Navigation.home.page_id
