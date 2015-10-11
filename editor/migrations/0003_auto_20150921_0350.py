# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0002_auto_20150921_0330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='class_id',
            new_name='yoga_class',
        ),
    ]
