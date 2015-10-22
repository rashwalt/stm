from django.http import HttpResponse
from django.template.loader import render_to_string

from apps.base.views.generic import BaseTemplateView, BaseUpdateView
from apps.base.navigation.enums import Navigation
from apps.memo.models import Label
from apps.memo.forms import LabelForm


class LabelListView(BaseTemplateView):
    template_name = 'apps/memo/label.html'
    page_id = Navigation.label.page_id

    def get_context_data(self, **kwargs):
        label_list = []
        for label in Label.objects.all():
            label.edit_form = LabelForm(instance=label)
            label_list.append(label)

        return {
            'label_list': label_list,
        }


class LabelEditView(BaseUpdateView):
    template_name = 'apps/memo/label_edit.html'
    template_success_name = 'apps/memo/label_edit_success.html'
    page_id = Navigation.label.page_id
    model = Label
    form_class = LabelForm
    label_id = None

    def dispatch(self, request, *args, **kwargs):
        self.label_id = kwargs['pk']
        return super(LabelEditView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        label = Label.objects.get(id=self.label_id)
        return HttpResponse(render_to_string(self.template_success_name, {'item': label}))
