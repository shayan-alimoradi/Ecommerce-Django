from django.test import TestCase

from shop_account.forms import (
    SignUpForm,
    SignInForm,
)


class TestSignUpForm(TestCase):
    def test_valid_data(self):
        form = SignUpForm(
            data={
                "username": "jack",
                "email": "jack@gmail.com",
                "password": 123,
                "confirm_password": 123,
            }
        )
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = SignUpForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)


class TestSignInForm(TestCase):
    def test_invalid_data(self):
        form = SignUpForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)
