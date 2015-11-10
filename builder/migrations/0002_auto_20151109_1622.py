# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ButtonType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Name of button', max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CSS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Name of CSS rule', max_length=255, null=True, blank=True)),
                ('selector', models.CharField(help_text=b'Selector', max_length=255, null=True, blank=True)),
                ('rule', models.CharField(help_text=b'Rule', max_length=2048, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='buttontype',
            name='css',
            field=models.ManyToManyField(to='builder.CSS', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='website',
            name='button_type',
            field=models.ForeignKey(blank=True, to='builder.ButtonType', null=True),
        ),
    ]
