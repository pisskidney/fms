# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='description',
        ),
        migrations.AddField(
            model_name='website',
            name='home_background',
            field=models.CharField(max_length=1024, blank=True),
        ),
        migrations.AddField(
            model_name='website',
            name='home_description',
            field=models.CharField(max_length=2048, blank=True),
        ),
        migrations.AddField(
            model_name='website',
            name='home_motto',
            field=models.CharField(max_length=1024, blank=True),
        ),
    ]
