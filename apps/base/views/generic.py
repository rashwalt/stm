from django.views.generic.base import TemplateResponseMixin
from django.views.generic import TemplateView, UpdateView


class BaseTemplateResponseMixin(TemplateResponseMixin):
    page_id = None

    def render_to_response(self, context, **response_kwargs):
        context['page_id'] = self.page_id
        return super(BaseTemplateResponseMixin, self).render_to_response(context, **response_kwargs)


class BaseTemplateView(TemplateView, BaseTemplateResponseMixin):
    pass


class BaseUpdateView(UpdateView, BaseTemplateResponseMixin):
    pass
