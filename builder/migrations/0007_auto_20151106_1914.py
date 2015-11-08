# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0006_theme'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theme',
            old_name='color_bg',
            new_name='color1',
        ),
        migrations.RenameField(
            model_name='theme',
            old_name='color_header',
            new_name='color2',
        ),
        migrations.RenameField(
            model_name='theme',
            old_name='color_links',
            new_name='color3',
        ),
        migrations.RenameField(
            model_name='theme',
            old_name='color_text',
            new_name='color4',
        ),
        migrations.RenameField(
            model_name='theme',
            old_name='color_text_header',
            new_name='color5',
        ),
    ]
