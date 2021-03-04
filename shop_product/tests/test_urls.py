from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shop_product.views import *


class TestUrls(SimpleTestCase):
    def test_product_list(self):
        url = reverse('product:list')
        self.assertEqual(resolve(url).func.view_class, ProductList)
    
    def test_product_detail(self):
        url = reverse('product:detail', args=['max', 7])
        self.assertEqual(resolve(url).func, product_detail)

    def test_add_favourite(self):
        url = reverse('product:fav', args=[7])
        self.assertEqual(resolve(url).func, add_favourite)

    def test_add_comment(self):
        url = reverse('product:comment', args=[7])
        self.assertEqual(resolve(url).func, add_comment)
    
    def test_favourite_list(self):
        url = reverse('product:fav-list')
        self.assertEqual(resolve(url).func, favourite_list)