from django.contrib import admin
from .models import Category, Product, Description, Property
from django.utils.safestring import mark_safe


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'external_id',
        'name',
    )
    list_display_links = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'image',
        'description',
        'get_html_photo',
    )
    list_display_links = ('name',)

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=100>")

    get_html_photo.short_description = "Миниатюра"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'image',
        'price',
        'min_description',
        'description',
    )

    list_display_links = ('name',)

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=100>")


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        'text',
    )

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=100>")
