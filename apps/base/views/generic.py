from django.views.generic import TemplateView


class BaseTemplateView(TemplateView):
    page_id = None

    def get_context_data(self, **kwargs):
        kwargs['page_id'] = self.page_id
        return super(BaseTemplateView, self).get_context_data(**kwargs)
