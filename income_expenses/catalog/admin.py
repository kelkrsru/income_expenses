from django.contrib import admin

from .models import GroupProduct, Product, Unit


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'is_active',
    )
    list_filter = (
        'group',
        'is_active',
    )
    list_editable = (
        'price',
        'is_active',
    )
    search_fields = (
        'name',
        'group',
    )


admin.site.register(GroupProduct)
admin.site.register(Product, ProductAdmin)
admin.site.register(Unit)
