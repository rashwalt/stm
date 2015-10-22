from colorsys import rgb_to_hsv
import webcolors

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

    @property
    def text_color(self):
        if self.color.startswith('#'):
            color = self.color
        else:
            color = webcolors.name_to_hex(self.color)

        color = color.strip()
        if color[0] == '#':
            color = color[1:]
        if len(color) != 6:
            raise ValueError("input #%s is not in #RRGGBB format" % color)

        r, g, b = color[:2], color[2:4], color[4:]
        r, g, b = [int(n, 16) for n in (r, g, b)]
        _, _, v = rgb_to_hsv(r / 255., g / 255., b / 255.)
        if v < 0.5:
            return '#fff'
        else:
            return '#333'
