# Core Django imports
from django.db import models
from django.core.validators import MaxValueValidator
from django.conf import settings

# 3rd-party imports
from django_jalali.db import models as jmodels

# Local import
from shop_product.models import Product, Variant


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    address = models.TextField()
    paid = models.BooleanField(default=False)
    created = jmodels.jDateTimeField(auto_now_add=True)
    discount = models.PositiveIntegerField(
        validators=[MaxValueValidator(100)], null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.created}"

    @property
    def get_total_price(self):
        total = sum(i.price() for i in self.order_item.all())
        if self.discount:
            discount_price = (self.discount * total) / 100
            return int(total - discount_price)
        return total


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT, related_name="order_item"
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    variant = models.ForeignKey(
        Variant, on_delete=models.PROTECT, null=True, blank=True
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"

    def price(self):
        if self.product.status is not None:
            return self.variant.total_price * self.quantity
        else:
            return self.product.total_price * self.quantity

    def get_color(self):
        return self.variant.color_variant

    get_color.short_description = "color"

    def get_size(self):
        return self.variant.size_variant

    get_size.short_description = "size"


class Coupon(models.Model):
    code = models.CharField(max_length=177, unique=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    active = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

    def __str__(self):
        return f"{self.code} - {self.discount}"
