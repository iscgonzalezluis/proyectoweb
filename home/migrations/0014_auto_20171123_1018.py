# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20171123_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='fechayhora',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='medicamento',
            name='hora',
            field=models.TimeField(auto_now=True),
        ),
    ]
