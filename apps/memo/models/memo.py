from apps.base import models
from .label import Label


class Memo(models.BaseMasterModel):
    label = models.ManyToManyField(Label, verbose_name='設定ラベル', blank=True)
    text = models.TextField('テキスト')

    def __str__(self):
        return self.text[:20]

    class Meta:
        verbose_name = 'メモ'
        verbose_name_plural = verbose_name
        select_on_save = True
        get_latest_by = 'updated'
