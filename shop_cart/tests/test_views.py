from django.test import TestCase, Client
from django.urls import reverse

from shop_cart.forms import CartForm


class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_cart_detail(self):
        response = self.client.get(reverse('cart:detail'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'cart/detail.html')
    
    def test_add_cart(self):
        response = self.client.post(reverse('cart:add', args=[1]))
        self.assertEqual(response.status_code, 403)
        self.failUnless(response.context['form'], CartForm)