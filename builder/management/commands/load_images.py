import os
from django.core.management.base import BaseCommand, CommandError
from builder.models import Image

class Command(BaseCommand):
    def handle(self, *args, **options):
        for f in os.listdir(os.getcwd() + '/static/imgs/bg'):
            if 'thumb' not in f and 'pre' not in f:
                base = 'imgs/bg/'
                name = f.replace('.jpg', '')
                name = base + name

                img = Image(
                    type='bg',
                    topic='nature',
                    thumbnail=name + '_thumb.png',
                    preview=name + '_preview.jpg',
                    full=name + '.jpg',
                )
                img.save()
                    
