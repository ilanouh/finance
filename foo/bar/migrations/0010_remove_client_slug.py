# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0009_auto_20160228_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='slug',
        ),
    ]
