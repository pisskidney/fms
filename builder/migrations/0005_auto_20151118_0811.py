# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0004_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layout',
            name='css',
            field=models.ManyToManyField(to='builder.CSS', blank=True),
        ),
    ]
