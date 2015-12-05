# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0002_auto_20151109_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Layout name', max_length=255, null=True, blank=True)),
                ('html', models.TextField(help_text=b'HTML', max_length=32000, null=True, blank=True)),
                ('type', models.IntegerField(default=1, null=True, blank=True, choices=[(1, b'Home'), (2, b'Services'), (3, b'Album'), (4, b'About'), (5, b'Contact')])),
            ],
        ),
        migrations.RemoveField(
            model_name='css',
            name='rule',
        ),
        migrations.RemoveField(
            model_name='css',
            name='selector',
        ),
        migrations.AddField(
            model_name='css',
            name='attr',
            field=models.CharField(help_text=b'Selector', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='css',
            name='select',
            field=models.CharField(help_text=b'Selector', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='css',
            name='val',
            field=models.CharField(help_text=b'Rule', max_length=2048, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='buttontype',
            name='css',
            field=models.ManyToManyField(to='builder.CSS', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='topic',
            field=models.CharField(blank=True, max_length=64, null=True, help_text=b'Image type. ex: background, logo etc...', choices=[(b'nature', b'Nature'), (b'social', b'Social'), (b'office', b'Office'), (b'night', b'Night'), (b'sun', b'Light'), (b'dark', b'Dark'), (b'fab', b'Fab'), (b'summer', b'Summer'), (b'misc', b'Misc')]),
        ),
        migrations.AlterField(
            model_name='website',
            name='build_stage',
            field=models.SmallIntegerField(default=1, help_text=b'1 - Name, 2 - Home Page, 3 - Contact', null=True, choices=[(1, b'Subdomain'), (2, b'Domain'), (3, b'Own domain')]),
        ),
        migrations.AlterField(
            model_name='website',
            name='owner',
            field=models.ForeignKey(related_name='websites', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='layout',
            name='css',
            field=models.ManyToManyField(to='builder.CSS', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='layout',
            name='img',
            field=models.ForeignKey(blank=True, to='builder.Image', null=True),
        ),
    ]
