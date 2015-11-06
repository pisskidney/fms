# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0003_auto_20151105_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='domain_type',
            field=models.SmallIntegerField(default=1, help_text=b'1 - Subdomain, 2 - TLD bought domain, 3 - Has own domain', null=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
