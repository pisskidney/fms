# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0008_auto_20151107_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='type',
            field=models.CharField(help_text=b'Image type', max_length=32, null=True, choices=[(b'bg', b'Background'), (b'bg_thumb', b'Background Thumb'), (b'bg_preview', b'Background Prewview')]),
        ),
    ]
