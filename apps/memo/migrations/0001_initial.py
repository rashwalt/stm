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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('color', apps.base.colorfield.fields.ColorField(max_length=10, verbose_name='カラー', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'ラベル',
                'select_on_save': True,
                'get_latest_by': 'updated',
                'verbose_name': 'ラベル',
            },
        ),
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(verbose_name='テキスト')),
                ('label', models.ManyToManyField(to='memo.Label', verbose_name='設定ラベル', blank=True)),
            ],
            options={
                'verbose_name_plural': 'メモ',
                'select_on_save': True,
                'get_latest_by': 'updated',
                'verbose_name': 'メモ',
            },
        ),
    ]
