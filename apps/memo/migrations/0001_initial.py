# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.base.colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='名称', max_length=100)),
                ('color', apps.base.colorfield.fields.ColorField(verbose_name='カラー', max_length=10)),
            ],
            options={
                'get_latest_by': 'updated',
                'select_on_save': True,
                'verbose_name_plural': 'ラベル',
                'verbose_name': 'ラベル',
            },
        ),
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(verbose_name='テキスト')),
                ('label', models.ManyToManyField(blank=True, verbose_name='設定ラベル', to='memo.Label')),
            ],
            options={
                'get_latest_by': 'updated',
                'select_on_save': True,
                'verbose_name_plural': 'メモ',
                'verbose_name': 'メモ',
            },
        ),
    ]
