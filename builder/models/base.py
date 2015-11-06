from django.db import models
from django.contrib.auth.models import User


TLD_CHOICES = (
    ('.com', '.com'),
    ('.net', '.net'),
)


class Website(models.Model):
    owner = models.ForeignKey(
        User,
        null=True
    )
    build_stage = models.SmallIntegerField(
        default=1,
        null=True,
        help_text='1 - Name, 2 - Home Page, 3 - Contact',
    )
    domain_name = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        help_text='The name of the domain ex: Google, DentistAssocNY',
    )
    domain_type = models.SmallIntegerField(
        default=1,
        null=True,
        help_text='1 - Subdomain, 2 - TLD bought domain, 3 - Has own domain',
    )
    title = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        help_text='The title of the website. ex: New York Architecs Assoc.',
    )

    home_motto = models.CharField(max_length=1024, blank=True)
    home_description = models.CharField(max_length=2048, blank=True)
    home_background = models.CharField(max_length=1024, blank=True)

    contact_email = models.EmailField(max_length=255, blank=True)
    contact_address = models.CharField(max_length=1024, blank=True)


class Album(models.Model):
    website = models.ForeignKey(Website)
    title = models.CharField(max_length=255, blank=False)
