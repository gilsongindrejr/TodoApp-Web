from django.test import TestCase

from users.models import CustomUserModel


class CustomUserModelTestCase(TestCase):

    def setUp(self):
        self.user = CustomUserModel.objects.create_user(
            email='user@email.com',
            password='4231',
            first_name='user',
            last_name='name',
            telephone='1233456789'
        )
        self.superuser = CustomUserModel.objects.create_superuser(email='superuser@email.com', password='4231')

    def test_str(self):
        self.assertEquals(str(self.user), self.user.email)

    def test_create_user(self):
        self.assertTrue(self.user, True)

    def test_create_user_exception(self):
        with self.assertRaises(ValueError):
            user = CustomUserModel.objects.create_user()

    def test_create_superuser(self):
        self.assertTrue(self.superuser, True)

    def test_create_superuser_exception1(self):
        with self.assertRaises(ValueError):
            superuser = CustomUserModel.objects.create_superuser(is_staff=False)

    def test_create_superuser_exception2(self):
        with self.assertRaises(ValueError):
            superuser = CustomUserModel.objects.create_superuser(is_superuser=False)
