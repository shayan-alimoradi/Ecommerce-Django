from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from shop_account.models import Profile
from shop_account.forms import (
    SignInForm,
    SignUpForm,
)

User = get_user_model()

class TestView(TestCase):
    def setup(self):
        self.client  = Client()
    
    def test_user_signup_GET(self):
        response = self.client.get(reverse('account:sign_up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/sign_up.html')
        self.failUnless(response.context['form'], SignUpForm)
    
    def test_user_signup_POST_valid(self):
        response = self.client.post(reverse('account:sign_up'), data={
            'username': 'anna',
            'email': 'anna@email.com',
            'password': '123',
            'confirm_password': '123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Profile.objects.count(), 1)

    def test_user_signup_POST_invalid(self):
        response = self.client.post(reverse('account:sign_up'), data={
            'username': 'jack',
            'email': 'invalidemail',
            'password': '123',
            'confirm_password': '123'
        })
        self.assertEqual(response.status_code, 200)
        self.failIf(response.context['form'].is_valid())
        self.assertFormError(response, 'form', field='email', errors=['please enter a valid email address'])

    # def test_user_profile_GET(self):
    #     self.client.login(email='max@email.com', password='max123')
    #     response = self.client.get(reverse('account:profile'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed('account/profile.html')

    def test_user_signin_GET(self):
        response = self.client.get(reverse('account:sign_in'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('account/sign_in.html')
        self.failUnless(response.context['form'], SignInForm)