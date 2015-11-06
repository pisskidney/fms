# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0004_auto_20151106_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='build_stage',
            field=models.SmallIntegerField(default=1, help_text=b'1 - Name, 2 - Home Page, 3 - Contact', null=True),
        ),
    ]
