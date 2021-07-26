from django.test import TestCase

from shop_cart.forms import (
    CartForm,
)


class TestCartForm(TestCase):
    def test_valid_data(self):
        form = CartForm(data={
            'quantity': 5
        })
        self.assertTrue(form.is_valid())
    
    def test_invalid_data(self):
        form = CartForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)