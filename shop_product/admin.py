from django.contrib.admin.models import ADDITION, LogEntry
from django.contrib import admin
from .models import *


class VariantInline(admin.TabularInline):
    model = Variant
    extra = 2
    readonly_fields = ('sell',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'unit_price', 'amount',
                    'discount', 'total_price', 'available', 'sell',
                    'category_to_str', 'get_visit_count', 'image_thumbnail')
    list_filter = ('available',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    inlines = (VariantInline,)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_sub', 'sub_cat')
    list_filter = ('is_sub',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, ProductAdmin)
LogEntry.objects.filter(action_flag=ADDITION)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Variant)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(Brand)