from django.test import SimpleTestCase
from django.urls import reverse, resolve

from shop_account import views


class TestUrls(SimpleTestCase):
    def test_sign_in(self):
        url = reverse('account:sign_in')
        self.assertEqual(resolve(url).func.view_class, views.SignIn)
    
    def test_sign_up(self):
        url = reverse('account:sign_up')
        self.assertEqual(resolve(url).func.view_class, views.SignUp)

    def test_sign_out(self):
        url = reverse('account:log_out')
        self.assertEqual(resolve(url).func.view_class, views.Logout)

    def test_profile(self):
        url = reverse('account:profile')
        self.assertEqual(resolve(url).func.view_class, views.UserProfile)

    def test_active_email(self):
        url = reverse('account:activate', args=['uidb64', 'token'])
        self.assertEqual(resolve(url).func.view_class, views.ActiveEmail)

    def test_change_password(self):
        url = reverse('account:change_pass')
        self.assertEqual(resolve(url).func.view_class, views.ChangePassword)

    def test_user_panel(self):
        url = reverse('account:user_panel')
        self.assertEqual(resolve(url).func.view_class, views.UserPanel)

    def test_history(self):
        url = reverse('account:history')
        self.assertEqual(resolve(url).func, views.history)