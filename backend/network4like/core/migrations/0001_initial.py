# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-27 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(default='', upload_to='', verbose_name='Arquivo')),
                ('qtd_likes', models.PositiveIntegerField(verbose_name='Quantidade de Likes')),
            ],
        ),
    ]
