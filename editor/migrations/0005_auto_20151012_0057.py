# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0004_auto_20150921_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pose',
            name='korean_name',
            field=models.CharField(default=None, max_length=256, blank=True),
        ),
        migrations.AlterField(
            model_name='pose',
            name='sanskrit_name',
            field=models.CharField(default=None, max_length=256, blank=True),
        ),
    ]
