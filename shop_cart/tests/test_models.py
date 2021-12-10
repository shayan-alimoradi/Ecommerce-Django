from django.test import TestCase
from django.contrib.auth import get_user_model

from shop_cart.models import Cart
from shop_product.models import Product, Variant

User = get_user_model()


class CartModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test",
            email="test@gmail.com",
        )
        self.product = Product.objects.create(
            title="lamborghini",
            description="someText",
            unit_price=7000,
            amount=20,
        )
        self.variant = Variant.objects.create(
            title="lamborghini black",
            unit_price=7000,
            amount=20,
        )
        self.cart = Cart.objects.create(
            user=self.user,
            product=self.product,
            variant=self.variant,
            quantity=7,
        )

    def test_user_content(self):
        self.cart = Cart.objects.get(id=1)
        expected_obj_name = f"{self.cart.user}"
        self.assertEqual(expected_obj_name, "test@gmail.com")

    def test_product_content(self):
        self.cart = Cart.objects.get(id=1)
        expected_obj_name = f"{self.cart.product.title}"
        self.assertEqual(expected_obj_name, "lamborghini")

    def test_variant_content(self):
        self.cart = Cart.objects.get(id=1)
        expected_obj_name = f"{self.cart.variant.title}"
        self.assertEqual(expected_obj_name, "lamborghini black")

    def test_quantity_content(self):
        self.cart = Cart.objects.get(id=1)
        expected_obj_name = f"{self.cart.quantity}"
        self.assertEqual(expected_obj_name, "7")
