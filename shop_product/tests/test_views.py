from django.test import TestCase, Client
from django.urls import reverse

from shop_product.models import (
    Product
)


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('product:list')
        self.detail_url = reverse('product:detail', args=['max', 1]) 

    def test_product_list(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_list.html')

    def test_product_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)