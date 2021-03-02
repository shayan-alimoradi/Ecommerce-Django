from django.contrib import admin
from .models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'product_to_str', 'active')
    list_filter = ('active',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Tag, TagAdmin)