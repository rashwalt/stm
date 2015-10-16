from apps.base.colorfield.fields import ColorField
from apps.base import models


class Label(models.BaseMasterModel):
    name = models.CharField('名称', max_length=100)
    color = ColorField('カラー', blank=True, null=True)

    def __str__(self):
        return '[{color}]: {name}'.format(color=self.color, name=self.name)

    class Meta:
        verbose_name = 'ラベル'
        verbose_name_plural = verbose_name
        select_on_save = True
        get_latest_by = 'modified'
