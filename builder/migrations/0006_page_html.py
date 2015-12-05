# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0005_auto_20151118_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='html',
            field=models.TextField(help_text=b'HTML', max_length=32000, null=True, blank=True),
        ),
    ]
