from django.test import TestCase, Client
from django.urls import reverse

from shop_cart.forms import CartForm


class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_cart_detail(self):
        response = self.client.get(reverse('cart:detail'))
        self.assertEqual(response.status_code, 302)
    
    def test_add_cart_POST_valid(self):
        response = self.client.post(reverse('cart:add', args=[1]), data={
            'quantity': 7
        })
        self.assertEqual(response.status_code, 302)
    
    def test_add_cart_POST_invalid(self):
        self.client.login(email='test@email.com', password='test')
        response = self.client.post(reverse('cart:add', args=[1]))
        self.assertEqual(response.status_code, 302)
        # self.failIf(response.context['form'].is_valid())
        # self.assertFormError(response, 'form', field='quantity', errors=[
        #     'This field is required'
        # ])