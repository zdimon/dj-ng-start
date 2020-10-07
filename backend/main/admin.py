from django.contrib import admin
from .models import *

class CatalogAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Catalog, CatalogAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'catalog']
    list_filter = ['catalog']

admin.site.register(Product, ProductAdmin)



