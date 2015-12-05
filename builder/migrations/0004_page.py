# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0003_auto_20151118_0737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Page name', max_length=255, null=True, blank=True)),
                ('priority', models.SmallIntegerField(null=True, blank=True)),
                ('layout', models.ForeignKey(to='builder.Layout')),
                ('website', models.ForeignKey(to='builder.Website')),
            ],
        ),
    ]
