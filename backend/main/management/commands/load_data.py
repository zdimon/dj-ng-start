from django.core.management.base import BaseCommand, CommandError
from main.models import *

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print('Load data')
        cats = ['Food', 'TV', 'Phone']
        for cat in cats:
            c = Catalog()
            c.name = cat
            c.save()
            for product in ['Test 1', 'Test 2', 'Test 3']:
                p = Product()
                p.name = product
                p.catalog = c
                p.save()