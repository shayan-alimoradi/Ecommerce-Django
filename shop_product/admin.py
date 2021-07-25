from django.contrib.admin.models import ADDITION, LogEntry
from django.shortcuts import redirect
from django.contrib import admin
from .models import (
    Product,
    Variant,
    Category,
    Size,
    Comment,
    Color,
    Brand,
)


class VariantInline(admin.TabularInline):
    model = Variant
    extra = 2
    readonly_fields = ('sell',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'unit_price',
        'available', 
        'view_sell',
        'category_to_str', 
        'get_visit_count', 
        'image_thumbnail'
    )
    list_filter = ('available',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    inlines = (VariantInline,)
    # add_form_template = 'product/form_change.html'

    def view_discount(self, obj):
        return obj.discount
    view_discount.empty_value_display = '???'
    view_discount.short_description = 'discount'

    def view_sell(self, obj):
        return obj.sell
    view_sell.admin_order_field = 'sell'
    view_sell.short_description = 'sell'

    def response_change(self, request, obj):
        if '_upper' in request.POST:
            obj.title = obj.title.upper()
            obj.save()
            self.message_user(request, 'object saved upper case', 'success')
            return redirect('admin:shop_product_product_changelist')
        return super().response_change(request, obj)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_sub', 'sub_cat')
    list_filter = ('is_sub',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Variant)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(Brand)