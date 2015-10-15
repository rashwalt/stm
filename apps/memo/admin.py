from django.contrib import admin
from .models import Memo, Label


@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    list_display = ('text', 'label_list')

    def label_list(self, row):
        return ','.join([x.name for x in row.label.all()])


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ["name", "color",]
