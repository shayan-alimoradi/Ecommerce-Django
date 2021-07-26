from django.test import TestCase

from shop_product.models import Product, Size


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
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