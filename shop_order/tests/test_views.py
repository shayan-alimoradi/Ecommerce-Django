from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from shop_order.forms import OrderForm
from shop_order.models import Order, OrderItem
from shop_product.models import Product, Variant

User = get_user_model()


class TestView(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create(
            username="test",
            email="test@gmail.com",
        )

    def test_cart_detail(self):
        response = self.client.get(reverse("order:detail", args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_order_create_POST_valid(self):
        response = self.client.post(
            reverse("order:create"), data={"user": self.user, "address": "Canada"}
        )
        self.assertEqual(response.status_code, 302)
