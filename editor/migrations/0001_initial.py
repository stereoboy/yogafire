# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pose',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('register_date', models.DateTimeField(auto_now=True)),
                ('english_name', models.CharField(max_length=256)),
                ('pose_image', models.ImageField(upload_to=b'pose_images')),
            ],
        ),
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('register_date', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(max_length=256)),
            ],
        ),
    ]
