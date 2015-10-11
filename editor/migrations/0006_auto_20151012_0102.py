# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0005_auto_20151012_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pose',
            name='korean_name',
            field=models.CharField(default=None, max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pose',
            name='sanskrit_name',
            field=models.CharField(default=None, max_length=256, null=True, blank=True),
        ),
    ]
