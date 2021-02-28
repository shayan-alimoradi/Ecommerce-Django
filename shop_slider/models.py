from django.db import models
from django.utils.html import format_html


class Slider(models.Model):
    title = models.CharField(max_length=177)
    description = models.TextField()
    image = models.ImageField(default='1.jpg')

    def __str__(self):
        return self.title
    
    def image_thumbnail(self):
        return format_html('<img src="{}" width=99>'.format(self.image.url))
    image_thumbnail.short_description = 'image'
    