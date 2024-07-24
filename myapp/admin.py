from django.contrib import admin
from . import models

class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'tag']
    list_editable = ['tag']
    list_filter = ['tag']

class ProductInformationAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'color', 'size']
    list_editable = ['color', 'size']
    list_filter = ['color', 'size']


class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']
    prepopulated_fields = {'slug': ['title']}
    list_display = [
        '__str__', 'title', 'price',
        'in_active', 'rating', 'category',
    ]
    list_editable = ['price', 'in_active', 'rating', 'category']
    list_filter = ['price', 'in_active', 'rating']


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'url']
    list_editable = ['title', 'url']
    list_filter = ['title', 'url']



admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory, ProductCategoryAdmin)
admin.site.register(models.ProductInformation, ProductInformationAdmin)
admin.site.register(models.ProductTag, ProductTagAdmin)


