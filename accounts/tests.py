from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="Testuser",
            email="test123@email.com",
            password="password123",
        )

        self.assertEqual(user.username, "Testuser")
        self.assertEqual(user.email, "test123@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="Testadmin",
            email="Admin123@email.com",
            password="Password123",
        )

        self.assertEqual(admin_user.username, "Testadmin")
        self.assertEqual(admin_user.email, "Admin123@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
