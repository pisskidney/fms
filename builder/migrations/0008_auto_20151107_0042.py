# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0007_auto_20151106_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(help_text=b'Image path', max_length=1024, null=True)),
                ('topic', models.CharField(help_text=b'Image topic. ex: business, nature', max_length=64, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='website',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
