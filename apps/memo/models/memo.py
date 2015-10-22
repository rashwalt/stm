from django.utils.lru_cache import lru_cache
from apps.base import models
from . import Label


class Memo(models.BaseMasterModel):
    label = models.ManyToManyField(Label, verbose_name='設定ラベル', blank=True)
    title = models.CharField('タイトル', max_length=100)
    text = models.TextField('テキスト')

    def __str__(self):
        return self.text[:20]

    class Meta:
        verbose_name = 'メモ'
        verbose_name_plural = verbose_name
        select_on_save = True
        get_latest_by = 'modified'

    @lru_cache()
    def labels(self):
        return self.label.all()
