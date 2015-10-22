# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='label',
            options={'verbose_name_plural': 'ラベル', 'select_on_save': True, 'get_latest_by': 'modified', 'verbose_name': 'ラベル'},
        ),
        migrations.AlterModelOptions(
            name='memo',
            options={'verbose_name_plural': 'メモ', 'select_on_save': True, 'get_latest_by': 'modified', 'verbose_name': 'メモ'},
        ),
        migrations.AddField(
            model_name='memo',
            name='title',
            field=models.CharField(default='No Title', max_length=100, verbose_name='タイトル'),
            preserve_default=False,
        ),
    ]
