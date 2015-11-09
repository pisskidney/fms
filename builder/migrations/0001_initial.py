# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thumbnail', models.CharField(help_text=b'Thumbnail path', max_length=1024, null=True, blank=True)),
                ('preview', models.CharField(help_text=b'Preview image path', max_length=1024, null=True, blank=True)),
                ('full', models.CharField(help_text=b'Full sized image path', max_length=1024, null=True, blank=True)),
                ('topic', models.CharField(blank=True, max_length=64, null=True, help_text=b'Image type. ex: background, logo etc...', choices=[(b'nature', b'Nature'), (b'social', b'Social'), (b'office', b'Office'), (b'night', b'Night'), (b'sun', b'Light')])),
                ('type', models.CharField(blank=True, max_length=64, null=True, help_text=b'Image topic. ex: business, nature etc...', choices=[(b'bg', b'Background'), (b'logo', b'Logo')])),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The name of the theme', max_length=255, null=True)),
                ('color1', models.CharField(help_text=b'Navbar color, text color', max_length=7)),
                ('color2', models.CharField(help_text=b'Button color', max_length=7)),
                ('color3', models.CharField(help_text=b'Navbar text color / button text color', max_length=7)),
                ('color4', models.CharField(help_text=b'Link color', max_length=7)),
                ('color5', models.CharField(help_text=b'', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('build_stage', models.SmallIntegerField(default=1, help_text=b'1 - Name, 2 - Home Page, 3 - Contact', null=True)),
                ('domain_name', models.CharField(help_text=b'The name of the domain ex: Google, DentistAssocNY', max_length=255, null=True)),
                ('domain_type', models.SmallIntegerField(default=1, help_text=b'1 - Subdomain, 2 - TLD bought domain, 3 - Has own domain', null=True)),
                ('title', models.CharField(help_text=b'The title of the website. ex: New York Architecs Assoc.', max_length=255, null=True)),
                ('home_motto', models.CharField(max_length=1024, blank=True)),
                ('home_description', models.CharField(max_length=2048, blank=True)),
                ('contact_email', models.EmailField(max_length=255, blank=True)),
                ('contact_address', models.CharField(max_length=1024, blank=True)),
                ('home_background', models.ForeignKey(blank=True, to='builder.Image', null=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('theme', models.ForeignKey(blank=True, to='builder.Theme', null=True)),
            ],
        ),
    ]
