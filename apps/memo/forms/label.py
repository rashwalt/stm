from django.forms import ModelForm

from apps.memo.models import Label


class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = '__all__'
