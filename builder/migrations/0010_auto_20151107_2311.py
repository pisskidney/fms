# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0009_image_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='path',
        ),
        migrations.RemoveField(
            model_name='image',
            name='type',
        ),
        migrations.AddField(
            model_name='image',
            name='full',
            field=models.CharField(help_text=b'Full sized image path', max_length=1024, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='preview',
            field=models.CharField(help_text=b'Preview image path', max_length=1024, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='thumbnail',
            field=models.CharField(help_text=b'Thumbnail path', max_length=1024, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='topic',
            field=models.CharField(blank=True, max_length=64, null=True, help_text=b'Image topic. ex: business, nature', choices=[(b'nature', b'Nature'), (b'social', b'Social'), (b'office', b'Office'), (b'dark', b'Dark'), (b'light', b'Light')]),
        ),
    ]
