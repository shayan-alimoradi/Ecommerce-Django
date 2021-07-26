from django.test import SimpleTestCase
from django.urls import reverse, resolve

from shop_cart import views


class TestUrls(SimpleTestCase):
    def test_cart_detail(self):
        url = reverse('cart:detail')
        self.assertEqual(resolve(url).func, views.cart_detail)
    
    def test_add_cart(self):
        url = reverse('cart:add', args=[7])
        self.assertEqual(resolve(url).func, views.add_cart)

    def test_compare_list(self):
        url = reverse('cart:compare_list')
        self.assertEqual(resolve(url).func, views.compare_list)

    def test_remove_cart(self):
        url = reverse('cart:remove', args=[7])
        self.assertEqual(resolve(url).func, views.remove_cart)
    
    def test_add_to_compare(self):
        url = reverse('cart:compare', args=[1])
        self.assertEqual(resolve(url).func, views.add_to_compare_list)
    
    def test_add_single(self):
        url = reverse('cart:add_sin', args=[1])
        self.assertEqual(resolve(url).func, views.add_single)

    def test_remove_single(self):
        url = reverse('cart:rem_sin', args=[1])
        self.assertEqual(resolve(url).func, views.remove_single)