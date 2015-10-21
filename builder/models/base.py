from django.db import models
from django.contrib.auth.models import User


class Website(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=1024, blank=False)

    contact_email = models.EmailField(max_length=255, blank=True)
    contact_address = models.CharField(max_length=1024, blank=True)


class Album(models.Model):
    website = models.ForeignKey(Website)
    title = models.CharField(max_length=255, blank=False)
