from django.db import models
from django.contrib.auth.models import User


TLD_CHOICES = (
    ('.com', '.com'),
    ('.net', '.net'),
)


class Theme(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        help_text='The name of the theme',
    )
    color1 = models.CharField(
        max_length=7,
        blank=False,
        help_text='Navbar color, text color',
    )
    color2 = models.CharField(
        max_length=7,
        blank=False,
        help_text='Button color',
    )
    color3 = models.CharField(
        max_length=7,
        blank=False,
        help_text='Navbar text color / button text color',
    )
    color4 = models.CharField(
        max_length=7,
        blank=False,
        help_text='Link color',
    )
    color5 = models.CharField(
        max_length=7,
        blank=False,
        help_text='',
    )


class Image(models.Model):

    IMAGE_TOPIC_CHOICES = (
        ('nature', 'Nature'),
        ('social', 'Social'),
        ('office', 'Office'),
        ('night', 'Night'),
        ('sun', 'Light'),
        ('dark', 'Dark'),
        ('fab', 'Fab'),
        ('summer', 'Summer'),
        ('misc', 'Misc'),
    )
    IMAGE_TYPE_CHOICES = (
        ('bg', 'Background'),
        ('logo', 'Logo'),
    )

    thumbnail = models.CharField(
        max_length=1024,
        blank=True,
        null=True,
        help_text='Thumbnail path',
    )
    preview = models.CharField(
        max_length=1024,
        blank=True,
        null=True,
        help_text='Preview image path',
    )
    full = models.CharField(
        max_length=1024,
        blank=True,
        null=True,
        help_text='Full sized image path',
    )
    topic = models.CharField(
        choices=IMAGE_TOPIC_CHOICES,
        max_length=64,
        blank=True,
        null=True,
        help_text='Image type. ex: background, logo etc...',
    )
    type = models.CharField(
        choices=IMAGE_TYPE_CHOICES,
        max_length=64,
        blank=True,
        null=True,
        help_text='Image topic. ex: business, nature etc...',
    )


class CSSBundle(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Name of CSS rule',
    )
    select = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Selector',
    )

    def __unicode__(self):
        return '%s // %s' % (self.name, self.select)


class CSS(models.Model):
    attr = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Selector',
    )
    val = models.CharField(
        max_length=2048,
        blank=True,
        null=True,
        help_text='Rule',
    )
    bundle = models.ForeignKey(
        'CSSBundle',
        blank=True,
        null=True
    )

    def __unicode__(self):
        return '%s: %s' % (self.attr, self.val)


class ButtonType(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Name of button',
    )
    css = models.ManyToManyField('CSS', blank=True)


class Website(models.Model):

    CHOICES_DOMAIN_TYPE = (
        (1, 'Subdomain'),
        (2, 'Domain'),
        (3, 'Own domain'),
    )

    owner = models.ForeignKey(
        User,
        null=True,
        related_name='websites',
    )
    build_stage = models.SmallIntegerField(
        default=1,
        null=True,
        choices=CHOICES_DOMAIN_TYPE,
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

    theme = models.ForeignKey('Theme', null=True, blank=True)

    button_type = models.ForeignKey('ButtonType', null=True, blank=True)

    home_motto = models.CharField(max_length=1024, blank=True)
    home_description = models.CharField(max_length=2048, blank=True)
    home_background = models.ForeignKey('Image', null=True, blank=True)

    contact_email = models.EmailField(max_length=255, blank=True)
    contact_address = models.CharField(max_length=1024, blank=True)

    @classmethod
    def create(cls):
        site = cls()
        site.save()
        page = Page.create_default(site)
        return site

    def __str__(self):
        return '%s. %s' % (self.id, self.domain_name)


class Layout(models.Model):
    CHOICES_LAYOUT_TYPE = (
        (1, 'Home'),
        (2, 'Services'),
        (3, 'Album'),
        (4, 'About'),
        (5, 'Contact'),
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Layout name',
    )
    html = models.TextField(
        max_length=32000,
        blank=True,
        null=True,
        help_text='HTML'
    )
    type = models.IntegerField(
        choices=CHOICES_LAYOUT_TYPE,
        default=1,
        null=True,
        blank=True,
    )

    img = models.ForeignKey('Image', null=True, blank=True)
    css = models.ManyToManyField('CSS', blank=True)

    @classmethod
    def default(cls):
        default = Layout.objects.filter(name='home').filter(type=1)
        return default[0]


class Page(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Page name',
    )
    priority = models.SmallIntegerField(
        blank=True,
        null=True,
    )
    layout = models.ForeignKey('Layout')
    website = models.ForeignKey('Website')
    html = models.TextField(
        max_length=32000,
        blank=True,
        null=True,
        help_text='HTML'
    )
    css = models.ManyToManyField('CSS', blank=True)

    @classmethod
    def create_default(cls, site):
        page = cls()
        page.name = 'Home'
        page.priority = 1
        page.layout = Layout.default()
        page.html = page.layout.html
        page.website = site
        page.save()
        page.css.add(*page.layout.css.all())
        return page
