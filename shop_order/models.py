from django.db import models
from shop_product.models import *
from shop_account.models import *
from django_jalali.db import models as jmodels


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    paid = models.BooleanField(default=False)
    created = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.created}'

    def get_total_price(self):
        pass


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.product.title}'