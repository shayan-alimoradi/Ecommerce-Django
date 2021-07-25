# Standard library import
from django.db import models
from django.utils.html import format_html
from django.utils.text import slugify
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings

# Third-party import
from django_jalali.db import models as jmodels


class TimeStamp(models.Model):
    created = jmodels.jDateTimeField(auto_now_add=True, null=True)
    updated = jmodels.jDateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address


class Category(TimeStamp):
    sub_cat = models.ForeignKey('self', on_delete=models.CASCADE, related_name='s_category', blank=True, null=True)
    is_sub = models.BooleanField(default=False)
    title = models.CharField(max_length=177)
    slug = models.SlugField(unique=True)

    class Meta(TimeStamp.Meta):
        ordering = ('-created',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('product:category', args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Product(TimeStamp):
    class STATUS(models.TextChoices):
        COLOR = 'c', 'color'
        SIZE = 's', 'size'
        NONE = 'n', 'none'
        BOTH = 'b', 'both'
    title = models.CharField(max_length=177)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    unit_price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(default='1.jpg')
    status = models.CharField(max_length=15, blank=True, choices=STATUS.choices)
    available = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=True)
    visit_count = models.ManyToManyField(IPAddress, blank=True, related_name='visit_count')
    favourite = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,
     related_name='fav')
    sell = models.PositiveIntegerField(default=0)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, blank=True, null=True)
    color = models.ManyToManyField('Color', blank=True)
    size = models.ManyToManyField('Size', blank=True)

    class Meta(TimeStamp.Meta):
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.total_price = self.get_total_price
        super().save(*args, **kwargs)
    
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
    

class Color(TimeStamp):
    title = models.CharField(max_length=177)

    def __str__(self):
        return self.title


class Size(TimeStamp):
    title = models.CharField(max_length=177)

    def __str__(self):
        return self.title


class Variant(TimeStamp):
    title = models.CharField(max_length=177)
    product_variant = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    size_variant = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True)
    color_variant = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    unit_price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField(null=True, blank=True)
    sell = models.PositiveIntegerField(default=0)

    class Meta(TimeStamp.Meta):
        ordering = ('-created',)

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
    
    def save(self, *args, **kwargs):
        self.total_price = self.get_total_price
        super().save(*args, **kwargs)
    
    def price_special_user(self):
        return self.total_price / 2


class Brand(TimeStamp):
    title = models.CharField(max_length=177)

    def __str__(self):
        return self.title


class Comment(TimeStamp):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    status = models.BooleanField(default=False)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, 
    blank=True, related_name='replies')
    is_reply = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.comment[:17]}'

    def children(self):
        return Comment.objects.filter(reply=self)