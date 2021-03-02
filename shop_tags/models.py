from django.db import models
from shop_product.models import *


class Tag(models.Model):
    title = models.CharField(max_length=177)
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True)
    product = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title
    
    def product_to_str(self):
        return '-'.join([product.title for product in self.product.all()])
    product_to_str.short_description = 'Products'