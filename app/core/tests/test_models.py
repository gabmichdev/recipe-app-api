from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email="test@example.com", password="test123"):
    """Create sample user"""
    return get_user_model().objects.create_user(email=email, password=password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = "test@test.com"
        password = "test123"
        user = get_user_model().objects.create_user(
            email=email, password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is  normalized"""
        email = "test@TEST.COM"
        user = get_user_model().objects.create_user(
            email=email, password="test123"
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            email = ""
            get_user_model().objects.create_user(
                email=email, password="test123"
            )

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        email = "test@test.com"
        password = "test123"
        user = get_user_model().objects.create_superuser(
            email=email, password=password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(user=sample_user(), name="vegan")

        self.assertEqual(str(tag), tag.name)
