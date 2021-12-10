from django.test import TestCase

from shop_order.forms import (
    OrderForm,
    CouponForm,
)


class TestOrderForm(TestCase):
    def test_valid_data(self):
        form = OrderForm(data={"address": "Canada"})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = OrderForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)


class TestCouponForm(TestCase):
    def test_valid_data(self):
        form = CouponForm(data={"code": "django"})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = OrderForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
