# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0008_auto_20151205_0455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='css',
            name='name',
        ),
        migrations.RemoveField(
            model_name='css',
            name='select',
        ),
    ]
