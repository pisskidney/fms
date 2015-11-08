# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0010_auto_20151107_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='type',
            field=models.CharField(blank=True, max_length=64, null=True, help_text=b'Image topic. ex: business, nature etc...', choices=[(b'bg', b'Background'), (b'logo', b'Logo')]),
        ),
        migrations.AlterField(
            model_name='image',
            name='topic',
            field=models.CharField(blank=True, max_length=64, null=True, help_text=b'Image type. ex: background, logo etc...', choices=[(b'nature', b'Nature'), (b'social', b'Social'), (b'office', b'Office'), (b'dark', b'Dark'), (b'light', b'Light')]),
        ),
    ]
