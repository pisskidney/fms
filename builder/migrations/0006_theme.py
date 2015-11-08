# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0005_website_build_stage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The name of the theme', max_length=255, null=True)),
                ('color_bg', models.CharField(max_length=7)),
                ('color_header', models.CharField(max_length=7)),
                ('color_text', models.CharField(max_length=7)),
                ('color_text_header', models.CharField(max_length=7)),
                ('color_links', models.CharField(max_length=7)),
            ],
        ),
    ]
