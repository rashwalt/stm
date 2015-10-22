from apps.base.views.generic import BaseTemplateView
from apps.base.navigation.enums import Navigation
from memo.models import Label


class LabelListView(BaseTemplateView):
    template_name = 'apps/memo/label.html'
    page_id = Navigation.label.page_id

    def get_context_data(self, **kwargs):
        return {
            'label_list': Label.objects.all(),
        }
