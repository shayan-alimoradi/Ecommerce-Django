from django.db import models
from django_jalali.db import models as jmodels
from django.utils.html import format_html
from django.urls import reverse
from shop_account.models import *


class TimeStamp(models.Model):
    created = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address


class Category(models.Model):
    sub_cat = models.ForeignKey('self', on_delete=models.CASCADE, related_name='s_category', blank=True, null=True)
    is_sub = models.BooleanField(default=False)
    title = models.CharField(max_length=177)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('product:category', args=[self.slug])


class Product(TimeStamp):
    VARIANT = (
        ('Color', 'color'),
        ('Size', 'size'),
        ('None', 'none'),
        ('Both', 'both'),
    )
    title = models.CharField(max_length=177)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    unit_price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField()
    image = models.ImageField(default='1.jpg')
    status = models.CharField(max_length=177, blank=True, choices=VARIANT)
    available = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=True)
    visit_count = models.ManyToManyField(IPAddress, blank=True, related_name='visit_count')
    favourite = models.ManyToManyField(User, blank=True, related_name='fav')
    sell = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    @property
    def get_total_price(self):
        if not self.discount:
            return self.unit_price
        elif self.discount:
            total = (self.discount * self.unit_price) / 100
            return int(self.unit_price - total)
        return self.total_price

    def image_thumbnail(self):
        return format_html('<img src="{}" width=77>'.format(self.image.url))
    
    def get_absolute_url(self):
        return reverse('product:detail', args=[self.slug, self.id])
    
    def category_to_str(self):
        return '-'.join([category.title for category in self.category.all()])
    category_to_str.short_description = 'Categories'

    def get_visit_count(self):
        return self.visit_count.count()
    get_visit_count.short_description = 'Visit Count'

    def price_special_user(self):
        return self.total_price / 2

class Color(models.Model):
    title = models.CharField(max_length=177)

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=177)

    def __str__(self):
        return self.title


class Variant(models.Model):
    title = models.CharField(max_length=177)
    product_variant = models.ForeignKey(Product, on_delete=models.CASCADE)
    size_variant = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True)
    color_variant = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    unit_price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField()
    sell = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    @property
    def get_total_price(self):
        if not self.discount:
            return self.unit_price
        elif self.discount:
            total = (self.discount * self.unit_price) / 100
            return int(self.unit_price - total)
        return self.total_price
    
    def price_special_user(self):
        return self.total_price / 2


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField()
    status = models.BooleanField(default=False)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    is_reply = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.comment[:17]}'