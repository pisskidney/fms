# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0002_auto_20151105_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='domain_name',
            field=models.CharField(help_text=b'The name of the domain ex: Google, DentistAssocNY', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='website',
            name='domain_type',
            field=models.SmallIntegerField(default=1, help_text=b'1 - Subdomain, 2 - TLD bought domain, 3 - has own domain', null=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='title',
            field=models.CharField(help_text=b'The title of the website. ex: New York Architecs Assoc.', max_length=255, null=True),
        ),
    ]
