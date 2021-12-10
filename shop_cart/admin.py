from django.contrib import admin

from .models import Cart, Compare


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("__str__", "variant", "quantity")
    search_fields = ("user", "product")


@admin.register(Compare)
class CompareAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "session_key")
    search_fields = ("user", "product")
