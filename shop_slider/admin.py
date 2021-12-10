from django.contrib import admin
from .models import *


class SliderAdmin(admin.ModelAdmin):
    list_display = ("title", "image_thumbnail")


admin.site.register(Slider, SliderAdmin)
