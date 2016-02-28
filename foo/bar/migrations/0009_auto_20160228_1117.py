# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0008_monthlyweatherbycity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MonthlyWeatherByCity',
        ),
        migrations.AddField(
            model_name='client',
            name='slug',
            field=models.SlugField(default='lol', unique=True, verbose_name='slug'),
            preserve_default=False,
        ),
    ]
