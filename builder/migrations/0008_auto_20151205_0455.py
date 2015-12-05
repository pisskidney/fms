# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0007_page_css'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSSBundle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Name of CSS rule', max_length=255, null=True, blank=True)),
                ('select', models.CharField(help_text=b'Selector', max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='css',
            name='bundle',
            field=models.ForeignKey(blank=True, to='builder.CSSBundle', null=True),
        ),
    ]
