"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails=[
            ['Test1@EXample.com','Test1@example.com'],
            ['Test2@EXample.com','Test2@example.com'],
            ['test3@EXample.com','test3@example.com'],
            ['Test4@EXample.Com','Test4@example.com'],
        ]
        for email,expected in sample_emails:
            user =get_user_model().objects.create_user(email,'Sample@112')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raise_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'Swing@132')
    def test_create_superuser(self):
        """ Testing creating super user"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'Stlap@143',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)