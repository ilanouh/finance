# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0010_remove_client_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productanalytic',
            name='period',
            field=models.CharField(max_length=250, verbose_name='period'),
        ),
    ]
