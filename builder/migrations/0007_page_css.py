# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0006_page_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='css',
            field=models.ManyToManyField(to='builder.CSS', blank=True),
        ),
    ]
