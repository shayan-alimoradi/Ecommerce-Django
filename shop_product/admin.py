from django.contrib import admin
from .models import *


class VariantInline(admin.TabularInline):
    model = Variant
    extra = 2


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'unit_price', 'amount', 'discount', 'total_price', 'available', 'image_thumbnail')
    list_filter = ('available',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    inlines = (VariantInline,)


admin.site.register(Product, ProductAdmin)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Variant)