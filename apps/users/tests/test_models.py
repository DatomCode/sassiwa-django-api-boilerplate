from django.test import TestCase
from apps.users.models import CustomUser


class CustomUserModelTest(TestCase):

    def setUp(self):
        self.email = "testemail@gmail.com"
        self.password = "testme@1234"

    def test_create_user(self):
        user = CustomUser.objects.create_user(
            email=self.email,
            password=self.password
        )

        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

