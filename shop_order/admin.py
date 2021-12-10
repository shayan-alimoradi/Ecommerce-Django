from django.contrib import admin

from .models import Order, OrderItem, Coupon


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = (
        "user",
        "order",
        "product",
        "variant",
        "get_color",
        "get_size",
        "quantity",
    )


class PaidListFilter(admin.SimpleListFilter):
    title = "Purchased"

    parameter_name = "paid"

    def lookups(self, request, model_admin):
        return (
            ("Paid", "paid"),
            ("Not Paid", "not paid"),
        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset

        elif self.value().lower() == "paid":
            return queryset.filter(paid=True)

        elif self.value().lower() == "not paid":
            return queryset.filter(paid=False)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "created", "paid")
    list_filter = (PaidListFilter,)
    inlines = (OrderItemInline,)


admin.site.register(OrderItem)
admin.site.register(Coupon)
