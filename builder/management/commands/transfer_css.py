import os
from django.core.management.base import BaseCommand, CommandError
from builder.models import CSSBundle, CSS

class Command(BaseCommand):
    def handle(self, *args, **options):
        for css in CSS.objects.all():
            if css.select:
                try:
                    bundle = CSSBundle.objects.filter(select__exact=css.select)[0]
                except IndexError:
                    print 'Creating CSSBundle(%s, %s)' % ('default_layout', css.select)
                    bundle = CSSBundle(name='default_layout', select=css.select)
                    bundle.save()

                print 'Adding CSS(%s, %s) to CSSBundle(%s, %s)' % (
                    css.attr, css.val, 'default_layout', css.select)
                css.bundle = bundle
                css.save()




