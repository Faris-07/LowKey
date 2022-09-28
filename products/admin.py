from .models import Product, Category
from django.contrib import admin

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    """ Category admin management """

    list_display = ("category_name", "name_to_display")


class ProductAdmin(admin.ModelAdmin):
    """ Product admin management """

    list_display = (
        "sku",
        "pk",
        "name",
        "category",
        "size",
        "price",
        "image",
        "category_id",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
