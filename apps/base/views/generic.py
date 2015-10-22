from django.views.generic import TemplateView


class BaseTemplateView(TemplateView):
    page_id = None

    def render_to_response(self, context, **response_kwargs):
        context['page_id'] = self.page_id
        return super(BaseTemplateView, self).render_to_response(context, **response_kwargs)
