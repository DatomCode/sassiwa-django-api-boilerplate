from django.test import TestCase
from apps.users.models import CustomUser


class CustomUserModelTest(TestCase):
    def setUp(self):
        self.email = "testuser@gmail.com"
        self.username = "testuser1"
        self.password = "password123"

    def test_create_user(self):
        user = CustomUser.objects.create_user(
            email=self.email, username=self.username, password=self.password
        )

        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_password_is_hashed(self):
        user = CustomUser.objects.create_user(
            email=self.email, username=self.username, password=self.password
        )

        self.assertNotEqual(user.password, self.password)
        self.assertTrue(user.check_password, self.password)

    def test_create_superuser(self):
        user = CustomUser.objects.create_superuser(
            email="admin@example.com", username="testadmin", password="password123"
        )

        self.assertEqual(user.email, "admin@example.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.check_password(self.password))
