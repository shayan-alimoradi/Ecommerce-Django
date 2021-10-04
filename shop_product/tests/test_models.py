from django.test import TestCase
from django.contrib.auth import get_user_model

from shop_product.models import Product, Size

User = get_user_model()


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testUser = User.objects.create(
            username='test',
            email='test@gmail.com',
            password=123,
        )
        testUser2 = User.objects.create(
            username='test2',
            email='test2@gmail.com',
            password=123,
        )
        Product.objects.create(
            title='lamborghini',
            description='someText',
            unit_price=7000,
            amount=50,
        )
    
    def test_title_content(self):
        product = Product.objects.get(id=1)
        expected_obj_name = f'{product.title}'
        self.assertEqual(expected_obj_name, 'lamborghini')

    def test_description_content(self):
        product = Product.objects.get(id=1)
        expected_obj_name = f'{product.description}'
        self.assertEqual(expected_obj_name, 'someText')

    def test_unit_price_content(self):
        product = Product.objects.get(id=1)
        expected_obj_name = f'{product.unit_price}'
        self.assertEqual(expected_obj_name, '7000')

    def test_amount_content(self):
        product = Product.objects.get(id=1)
        expected_obj_name = f'{product.amount}'
        self.assertEqual(expected_obj_name, '50')

    def test_favourite_product_users(self):
        user1 = User.objects.get(pk=1)
        user2 = User.objects.get(pk=2)
        title = Product.objects.get(id=1)
        title.favourite.set([user1.pk, user2.pk])
        self.assertEqual(title.favourite.count(), 2)