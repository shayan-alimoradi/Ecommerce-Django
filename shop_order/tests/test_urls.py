from django.test import SimpleTestCase
from django.urls import reverse, resolve

from shop_order import views


class TestUrls(SimpleTestCase):
    def test_order_detail(self):
        url = reverse("order:detail", args=[7])
        self.assertEqual(resolve(url).func, views.order_detail)

    def test_create_order(self):
        url = reverse("order:create")
        self.assertEqual(resolve(url).func, views.create_order)

    def test_coupon_order(self):
        url = reverse("order:coupon", args=[1])
        self.assertEqual(resolve(url).func, views.coupon_order)

    def test_send_request(self):
        url = reverse("order:request", args=[5000, 7])
        self.assertEqual(resolve(url).func, views.send_request)

    def test_fverify(self):
        url = reverse("order:verify")
        self.assertEqual(resolve(url).func, views.verify)
