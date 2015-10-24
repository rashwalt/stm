from django.views.generic.base import TemplateResponseMixin
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView


class GenericTemplateResponseMixin(TemplateResponseMixin):
    page_id = None

    def render_to_response(self, context, **response_kwargs):
        context['page_id'] = self.page_id
        return super(GenericTemplateResponseMixin, self).render_to_response(context, **response_kwargs)


class GenericTemplateView(TemplateView, GenericTemplateResponseMixin):
    pass


class GenericUpdateView(UpdateView, GenericTemplateResponseMixin):
    pass


class GenericDeleteView(DeleteView, GenericTemplateResponseMixin):
    pass


class GenericCreateView(CreateView, GenericTemplateResponseMixin):
    pass
