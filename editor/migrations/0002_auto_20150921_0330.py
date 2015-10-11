# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('nick_name', models.CharField(default=b'', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('author', models.ForeignKey(to='editor.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('author', models.ForeignKey(to='editor.Author')),
                ('class_id', models.ForeignKey(to='editor.Class')),
            ],
        ),
        migrations.AddField(
            model_name='pose',
            name='parents',
            field=models.ManyToManyField(related_name='parents_rel_+', to='editor.Pose'),
        ),
        migrations.AddField(
            model_name='sequence',
            name='pose',
            field=models.ForeignKey(default=None, to='editor.Pose'),
        ),
    ]
