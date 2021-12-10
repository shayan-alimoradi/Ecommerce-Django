from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            username="max",
            email="max@email.com",
        )

    def test_username_content(self):
        user = User.objects.get(id=1)
        expected_obj_name = f"{user.username}"
        self.assertEqual(expected_obj_name, "max")

    def test_email_content(self):
        user = User.objects.get(id=1)
        expected_obj_name = f"{user.email}"
        self.assertEqual(expected_obj_name, "max@email.com")
